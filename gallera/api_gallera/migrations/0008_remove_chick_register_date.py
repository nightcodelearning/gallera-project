# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_gallera', '0007_auto_20170912_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chick',
            name='register_date',
        ),
    ]
