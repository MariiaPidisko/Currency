from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=35)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
