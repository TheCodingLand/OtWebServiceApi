# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot_webservice_api', '0007_auto_20171109_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='history',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
