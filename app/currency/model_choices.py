from django.db import models


class RateType(models.TextChoices):
    USD = 'USD', 'Dollar'
    EUR = 'EUR', 'Euro'


# class SourceCodeName(models.IntegerChoices):
#     PRIVATBANK = 1, 'PrivatBank'
#     MONOBANK = 2, 'Monobank'


# RATE_TYPE_USD = 'USD'
# RATE_TYPE_EUR = 'EUR'
#
# RATE_TYPES = (
#     (RATE_TYPE_USD, 'Dollar'),
#     (RATE_TYPE_EUR, 'Euro'),
# )
