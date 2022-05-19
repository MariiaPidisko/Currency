from currency import model_choices as mch

from django.db import models
from django.templatetags.static import static


class Rate(models.Model):
    type = models.CharField(max_length=10, choices=mch.RateType.choices)   # noqa: A003
    created = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=35)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)


def upload_logo(instance, filename: str) -> str:
    return f'{instance.name}/logos/{filename}'


class Source(models.Model):
    source_url = models.URLField(max_length=100)
    name = models.CharField(max_length=50, unique=True)
    contact_number = models.DecimalField(max_digits=25, decimal_places=0)

    logo = models.FileField(upload_to=upload_logo, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def logo_url(self):
        if self.logo:
            return self.logo.url

        return static('img/logo-placeholder')
