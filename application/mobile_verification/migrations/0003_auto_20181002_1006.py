# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_verification', '0002_auto_20181002_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='token',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
