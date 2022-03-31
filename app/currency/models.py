from django.db import models


class Rate(models.Model):
    type = models.CharField(max_length=10)   # noqa: A003
    source = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=35)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)


class Source(models.Model):
    source_url = models.URLField(max_length=100)
    name = models.CharField(max_length=50)
    contact_number = models.DecimalField(max_digits=25, decimal_places=0)
