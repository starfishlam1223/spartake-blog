# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-26 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20171026_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='imageslug',
        ),
    ]
