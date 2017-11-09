# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ot_webservice_api', '0006_auto_20171109_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='history',
            field=models.DateTimeField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ot_webservice_api.Agent'),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='destination',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='end',
            field=models.DateTimeField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='origin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='start',
            field=models.DateTimeField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]