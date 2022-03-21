# Generated by Django 4.0.2 on 2022-03-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('source', models.CharField(max_length=20)),
                ('created', models.DateTimeField()),
                ('bye', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
