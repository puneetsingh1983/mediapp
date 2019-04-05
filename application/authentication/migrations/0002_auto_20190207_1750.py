# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-07 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appusermodel',
            old_name='modifile_on',
            new_name='modified_on',
        ),
        migrations.AddField(
            model_name='appusermodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appusermodel',
            name='user_status',
            field=models.IntegerField(choices=[('pending_approval', 'Approval Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('on_hold', 'On Hold')], default='pending_approval'),
        ),
        migrations.AlterField(
            model_name='appusermodel',
            name='user_type',
            field=models.IntegerField(choices=[('', ' -- '), ('doctor', 'Doctor'), ('health_worker', 'Health Worker'), ('patient', 'Patient'), ('medical_rep', 'Medical Representative'), ('other', 'Other')], default=''),
        ),
    ]
