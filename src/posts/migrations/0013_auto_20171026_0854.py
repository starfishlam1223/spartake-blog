# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-26 08:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20171026_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 10, 26, 8, 54, 54, 605629, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postimage',
            name='imageid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]
