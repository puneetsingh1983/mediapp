# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-17 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_remove_address_country'),
        ('userprofile', '0011_auto_20190210_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='availability_mode',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline'), ('out_door', 'Out Door')], default=1, max_length=9),
        )
    ]
