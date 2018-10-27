# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import helper.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=10, validators=[helper.validators.mobile_validator])),
                ('contact_person', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('gst_no', models.CharField(max_length=15)),
                ('license_no', models.CharField(max_length=25)),
                ('head_of_department', models.CharField(blank=True, max_length=50, null=True)),
                ('license_doc', models.FileField(upload_to='documents/org/%Y/%m/%d/')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Address')),
                ('associated_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='org_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.OrganizationType'),
        ),
        migrations.AddField(
            model_name='organization',
            name='qualifications',
            field=models.ManyToManyField(to='common.Qualification'),
        ),
    ]
