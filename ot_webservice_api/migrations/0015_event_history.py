# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot_webservice_api', '0014_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='history',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
