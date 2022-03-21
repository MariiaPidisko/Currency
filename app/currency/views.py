from currency.models import ContactUs
from currency.models import Rate

from django.shortcuts import render


def rate_list(request):
    rates = Rate.objects.all()
    return render(request, 'rate_list.html', context={'rates': rates})


def cont_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'cont_list.html', context={'contacts': contacts})


def index(request):
    return render(request, 'index.html')
