# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_gallera', '0009_auto_20170913_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
