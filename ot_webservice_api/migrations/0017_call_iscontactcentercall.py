# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot_webservice_api', '0016_auto_20171110_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='isContactCenterCall',
            field=models.BooleanField(default=False),
        ),
    ]
