# Generated by Django 4.0.2 on 2022-05-14 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_source_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='code_name',
        ),
    ]
