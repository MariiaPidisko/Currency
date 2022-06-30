# Generated by Django 4.0.2 on 2022-06-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_alter_source_code_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='code_name',
            field=models.PositiveSmallIntegerField(choices=[(1, 'PrivatBank'), (2, 'MonoBank'), (3, 'Vkurse'), (4, 'Credit_Agricole'), (5, 'UkrsibBank')], unique=True),
        ),
    ]
