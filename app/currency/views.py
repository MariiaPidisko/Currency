from currency.models import ContactUs

from django.shortcuts import render


def cont_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'cont_list.html', context={'contacts': contacts})


def index(request):
    return render(request, 'index.html')
