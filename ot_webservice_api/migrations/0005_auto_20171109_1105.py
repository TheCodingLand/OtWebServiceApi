# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot_webservice_api', '0004_auto_20171109_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='login',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
