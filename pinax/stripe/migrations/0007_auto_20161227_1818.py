# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0006_accounts_transfers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='business_primary_color',
        ),
        migrations.RemoveField(
            model_name='account',
            name='support_url',
        ),
        migrations.AlterField(
            model_name='account',
            name='business_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='business_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]