# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-26 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20181028_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='common.Address'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='associated_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organization.Organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organization.OrganizationType'),
        ),
    ]
