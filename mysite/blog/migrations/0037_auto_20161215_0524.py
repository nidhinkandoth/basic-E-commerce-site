# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 05:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20161215_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postssubmit',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 15, 5, 24, 42, 667929, tzinfo=utc)),
        ),
    ]