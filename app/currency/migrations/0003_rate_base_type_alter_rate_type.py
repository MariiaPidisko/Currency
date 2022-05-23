# Generated by Django 4.0.2 on 2022-05-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_source_contact_number_alter_source_source_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='base_type',
            field=models.CharField(choices=[('UAH', 'Hrivna'), ('USD', 'Dollar'), ('EUR', 'Euro'), ('BTC', 'Bitcoin')], default='UAH', max_length=10),
        ),
        migrations.AlterField(
            model_name='rate',
            name='type',
            field=models.CharField(choices=[('UAH', 'Hrivna'), ('USD', 'Dollar'), ('EUR', 'Euro'), ('BTC', 'Bitcoin')], max_length=10),
        ),
    ]
