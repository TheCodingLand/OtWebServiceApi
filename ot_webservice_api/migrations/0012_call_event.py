# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ot_webservice_api', '0011_remove_event_call'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ot_webservice_api.Event'),
        ),
    ]
