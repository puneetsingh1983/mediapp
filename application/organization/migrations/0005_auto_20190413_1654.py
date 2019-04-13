# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 16:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0004_auto_20190217_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_created_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organization',
            name='edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_edited_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.Address'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='associated_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='organization.Organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.OrganizationType'),
        ),
    ]
