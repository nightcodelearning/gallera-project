# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_gallera', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chick',
            old_name='name',
            new_name='castador_name',
        ),
        migrations.RemoveField(
            model_name='chick',
            name='description',
        ),
        migrations.RemoveField(
            model_name='chick',
            name='idempotency_token',
        ),
        migrations.RemoveField(
            model_name='chick',
            name='tag',
        ),
        migrations.AddField(
            model_name='chick',
            name='castador_tag',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='chick',
            name='coliseo_tag',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='chick',
            name='register_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='chick',
            name='tagger_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
