# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20170320_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='youtube_id',
        ),
        migrations.AlterField(
            model_name='source',
            name='id',
            field=models.CharField(editable=False, max_length=150, primary_key=True, serialize=False),
        ),
    ]
