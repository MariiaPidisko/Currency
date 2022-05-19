from currency.models import Rate, Source

from django import forms


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('type', 'source', 'buy', 'sale')


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ('logo', 'source_url', 'name', 'contact_number')
