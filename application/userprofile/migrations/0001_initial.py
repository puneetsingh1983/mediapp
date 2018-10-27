# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import helper.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('availability_mode', models.IntegerField(choices=[(1, 'Online'), (2, 'Offline'), (3, 'Out Door')], default=2)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('online_chat', models.NullBooleanField()),
                ('online_video_call', models.NullBooleanField()),
                ('online_voice_call', models.NullBooleanField()),
                ('outdoor_travel_upto', models.PositiveIntegerField()),
                ('outdoor_travel_city', models.CharField(max_length=50)),
                ('outdoor_travel_locality', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=10, validators=[helper.validators.mobile_validator])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('husband_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[('-', ' -- '), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=1, max_length=1)),
                ('unique_id', models.UUIDField(default=uuid.UUID('5789a6a6-5708-42f0-91b7-d52c8e65c531'), editable=False, unique=True)),
                ('registration_number', models.CharField(max_length=25)),
                ('years_of_experience', models.IntegerField()),
                ('resume', models.FileField(blank=True, null=True, upload_to='documents/doctor/')),
                ('registration_certificate', models.FileField(upload_to='documents/doctor/')),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='documents/doctor/')),
                ('Research', models.ManyToManyField(blank=True, null=True, to='common.Research')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Address')),
                ('associated_with', models.ManyToManyField(blank=True, null=True, to='organization.Organization')),
                ('languages_can_speak', models.ManyToManyField(to='common.Language')),
                ('qualification', models.ManyToManyField(to='common.Qualification')),
                ('specialization', models.ManyToManyField(to='common.Specialization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthworkerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('husband_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[('-', ' -- '), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=1, max_length=1)),
                ('unique_id', models.UUIDField(default=uuid.UUID('5789a6a6-5708-42f0-91b7-d52c8e65c531'), editable=False, unique=True)),
                ('registration_number', models.CharField(max_length=25)),
                ('years_of_experience', models.IntegerField()),
                ('resume', models.FileField(blank=True, null=True, upload_to='documents/healthworker/')),
                ('registration_certificate', models.FileField(upload_to='documents/healthworker/')),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='documents/healthworker/')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Address')),
                ('associated_with', models.ManyToManyField(to='organization.Organization')),
                ('languages_can_speak', models.ManyToManyField(to='common.Language')),
                ('qualification', models.ManyToManyField(to='common.Qualification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalRepresentative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('husband_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[('-', ' -- '), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=1, max_length=1)),
                ('unique_id', models.UUIDField(default=uuid.UUID('5789a6a6-5708-42f0-91b7-d52c8e65c531'), editable=False, unique=True)),
                ('registration_certificate', models.FileField(upload_to='documents/medicalrepresentative/')),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='documents/medicalrepresentative/')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Address')),
                ('associated_with', models.ManyToManyField(to='organization.Organization')),
                ('qualification', models.ManyToManyField(to='common.Qualification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('husband_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[('-', ' -- '), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=1, max_length=1)),
                ('unique_id', models.UUIDField(default=uuid.UUID('5789a6a6-5708-42f0-91b7-d52c8e65c531'), editable=False, unique=True)),
                ('case_summary', models.TextField(blank=True, null=True)),
                ('weight', models.PositiveIntegerField(help_text='in Kilogram')),
                ('height', models.PositiveIntegerField(help_text='in Centimeters')),
                ('aadhaar_no', models.PositiveIntegerField(blank=True, null=True)),
                ('alternate_mobile_no', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Address')),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.BloodGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='availability',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.DoctorProfile'),
        ),
        migrations.AddField(
            model_name='availability',
            name='health_worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.HealthworkerProfile'),
        ),
        migrations.AddField(
            model_name='availability',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
        ),
    ]
