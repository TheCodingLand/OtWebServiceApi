# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot_webservice_api', '0015_event_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='history',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
