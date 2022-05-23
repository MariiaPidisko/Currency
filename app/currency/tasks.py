from celery import shared_task

from currency import model_choices as mch

from decimal import Decimal

import requests


def round_decimal(value: str) -> Decimal:
    places = Decimal(10) ** -2
    return Decimal(value).quantize(places)


@shared_task
def parse_privatbank():

    from currency.models import Rate, Source

    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currencies = {
        'USD': mch.RateType.USD,
        'EUR': mch.RateType.EUR,
        'BTC': mch.RateType.BTC,
        'UAH': mch.RateType.UAH,
    }

    source, created = Source.objects.get_or_create(source_url='https://privatbank.ua',
                                                   code_name=mch.SourceCodeName.PRIVATBANK,
                                                   contact_number='3700')[0]

    for rate in rates:
        currency_type = available_currencies.get(rate['ccy'])
        if not currency_type:
            breakpoint()
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
