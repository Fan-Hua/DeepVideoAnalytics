# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0006_auto_20170411_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='vdndataset',
            name='root',
            field=models.BooleanField(default=True),
        ),
    ]
