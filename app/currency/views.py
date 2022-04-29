from currency.forms import RateForm, SourceForm
from currency.models import ContactUs
from currency.models import Rate
from currency.models import Source

from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class RateList(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreate(CreateView):
    model = Rate
    template_name = 'rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateUpdate(UserPassesTestMixin, UpdateView):
    model = Rate
    template_name = 'rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDelete(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactList(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'cont_list.html'


class ContactUsCreate(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'email_from',
        'subject',
        'message',
    )

    def _send_email(self):
        recipient = settings.EMAIL_HOST_USER
        subject = 'User ContactUs'
        body = f'''
            Email_from: {self.object.email_from}
            Subject: {self.object.subject}
            Message: {self.object.message}
        '''
        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


class SourceList(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreate(CreateView):
    model = Source
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceUpdate(UserPassesTestMixin, UpdateView):
    model = Source
    template_name = 'source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')

    def test_func(self):
        return self.request.user.is_superuser


class SourceDelete(UserPassesTestMixin, DeleteView):
    queryset = Source.objects.all()
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_list')

    def test_func(self):
        return self.request.user.is_superuser
