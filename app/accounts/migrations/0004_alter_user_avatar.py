# Generated by Django 4.0.2 on 2022-05-22 08:58

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, default=None, null=True, upload_to=accounts.models.upload_avatar),
        ),
    ]
