from decimal import Decimal

from celery import shared_task

from currency import model_choices as mch

import requests


def round_decimal(value: str) -> Decimal:
    places = Decimal(10) ** -2
    return Decimal(value).quantize(places)


@shared_task
def parse_privatbank():

    from currency.models import Rate, Source

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currencies = {
        'USD': mch.RateType.USD,
        'EUR': mch.RateType.EUR,
        'BTC': mch.RateType.BTC,
        'UAH': mch.RateType.UAH,
    }

    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.PRIVATBANK)[0]

    for rate in rates:
        currency_type = available_currencies.get(rate['ccy'])
        if not currency_type:
            continue

        base_currency_type = available_currencies.get(rate['base_ccy'])

        sale = round_decimal(rate["sale"])
        buy = round_decimal(rate["buy"])

        last_rate = Rate.objects\
            .filter(source=source, type=currency_type)\
            .order_by('-created').first()

        if (last_rate is None or  # does not exist in table
                last_rate.sale != sale or
                last_rate.buy != buy):
            Rate.objects.create(
                type=currency_type,
                base_type=base_currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_monobank():

    from currency.models import Rate, Source

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currencies = {
        980: mch.RateType.UAH,
        840: mch.RateType.USD,
        978: mch.RateType.EUR,
    }

    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.MONOBANK)[0]

    for rate in rates:
        currency_type = available_currencies.get(rate['currencyCodeA'])
        if not currency_type:
            continue

        base_currency_type = available_currencies.get(rate['currencyCodeB'])

        sale = round_decimal(rate["rateSell"])
        buy = round_decimal(rate["rateBuy"])

        last_rate = Rate.objects\
            .filter(source=source, type=currency_type)\
            .order_by('-created').first()

        if (last_rate is None or  # does not exist in table
                last_rate.sale != sale or
                last_rate.buy != buy):
            Rate.objects.create(
                type=currency_type,
                base_type=base_currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_vkurse():

    from currency.models import Rate, Source

    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currencies = {
        'Dollar': mch.RateType.USD,
        'Euro': mch.RateType.EUR,
    }

    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.VKURSE)[0]

    for currency_type, rate in rates.items():
        if currency_type in available_currencies:
            sale = round_decimal(rate['sale'])
            buy = round_decimal(rate['buy'])
        if currency_type not in available_currencies:
            continue

        last_rate = Rate.objects.filter(source=source, type=currency_type).order_by('-created').first()

        if (last_rate is None or  # does not exist in table
                last_rate.sale != sale or
                last_rate.buy != buy):
            Rate.objects.create(
                type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_credit_agricole():

    from bs4 import BeautifulSoup
    from currency.models import Rate, Source

    url = 'https://credit-agricole.ua/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    rates_table = soup.find(class_="exchange-rates-table")

    available_currencies = {
        'USD': mch.RateType.USD,
        'EUR': mch.RateType.EUR,
    }

    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.CREDIT_AGRICOLE)[0]

    rates = rates_table.find("tbody").find_all("tr")
    for i in range(len(rates)):
        rate = rates[i].text.split()

        currency_type = rate[0]

        if currency_type in available_currencies:
            buy = round_decimal(rate[1])
            sale = round_decimal(rate[2])

        if currency_type not in available_currencies:
            continue

        last_rate = Rate.objects.filter(source=source, type=currency_type).order_by('-created').first()

        if (last_rate is None or  # does not exist in table
                last_rate.sale != sale or
                last_rate.buy != buy):
            Rate.objects.create(
                type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_ukrsibbank():

    from bs4 import BeautifulSoup
    from currency.models import Rate, Source
    import re

    url = 'https://my.ukrsibbank.com/ua/personal/operations/currency_exchange/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    rates_table = soup.find(class_="currency__table")

    available_currencies = {
        'USD, долар США': mch.RateType.USD,
        'EUR, євро': mch.RateType.EUR,
    }

    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.UKRSIBBANK)[0]

    rates = rates_table.find("tbody").find_all("tr")
    for rate_list in rates:
        rate = rate_list.find_all("td")

        currency_type = rate[0].get_text()

        if currency_type in available_currencies:
            buy = round_decimal(re.sub("[^0-9.]", "", rate[1].get_text()))
            sale = round_decimal(re.sub("[^0-9.]", "", rate[2].get_text()))

        if currency_type not in available_currencies:
            continue

        last_rate = Rate.objects.filter(source=source, type=currency_type).order_by('-created').first()

        if (last_rate is None or  # does not exist in table
                last_rate.sale != sale or
                last_rate.buy != buy):
            Rate.objects.create(
                type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_creditdnepr():

    from bs4 import BeautifulSoup
    from currency.models import Rate, Source

    url = 'https://creditdnepr.com.ua/currency'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    rates_table = soup.find_all(class_="table-s1 tac sticky-enabled")[1]

    available_currencies = {
        'USD': mch.RateType.USD,
        'EUR': mch.RateType.EUR,
    }

    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.KREDITDNEPR)[0]

    rates = rates_table.find("tbody").find_all("tr")
    for rate_list in rates:
        rate = rate_list.find_all("td")

        currency_type = available_currencies.get(rate[0].get_text())

        if not currency_type:
            continue

        buy = round_decimal(rate[1].get_text())
        sale = round_decimal(rate[2].get_text())

        last_rate = Rate.objects.filter(source=source, type=currency_type).order_by('-created').first()

        if (last_rate is None or  # does not exist in table
                last_rate.sale != sale or
                last_rate.buy != buy):
            Rate.objects.create(
                type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )
