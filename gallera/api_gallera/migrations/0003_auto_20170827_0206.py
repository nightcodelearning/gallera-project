# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 02:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_gallera', '0002_auto_20170827_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chick',
            old_name='register_date',
            new_name='born_date',
        ),
    ]