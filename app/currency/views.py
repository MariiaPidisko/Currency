from currency.forms import SourceForm
from currency.models import ContactUs
from currency.models import Rate
from currency.models import Source

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class RateList(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class ContactList(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'cont_list.html'


class SourceList(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreate(CreateView):
    model = Source
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceUpdate(UpdateView):
    model = Source
    template_name = 'source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDelete(DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_list')
