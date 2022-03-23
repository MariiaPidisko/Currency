from currency.forms import SourceForm
from currency.models import ContactUs
from currency.models import Rate
from currency.models import Source

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def rate_list(request):
    rates = Rate.objects.all()
    return render(request, 'rate_list.html', context={'rates': rates})


def cont_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'cont_list.html', context={'contacts': contacts})


def source_list(request):
    sources = Source.objects.all()
    return render(request, 'source_list.html', context={'sources': sources})


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    else:
        form = SourceForm()

    return render(request, 'source_create.html', context={'form': form})


def source_update(request, pk):
    instance = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    else:
        form = SourceForm(instance=instance)

    return render(request, 'source_update.html', context={'form': form})


def source_delete(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect('/source/list')
    else:
        return render(request, 'source_delete.html', context={'source': instance})


def index(request):
    return render(request, 'index.html')
