# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161214_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postssubmit',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 14, 10, 43, 11, 547805, tzinfo=utc)),
        ),
    ]