# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 07:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='review',
            field=models.CharField(default=datetime.datetime(2017, 7, 17, 7, 27, 44, 461000, tzinfo=utc), max_length=225),
            preserve_default=False,
        ),
    ]