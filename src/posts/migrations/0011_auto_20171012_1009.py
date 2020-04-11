# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-12 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
    ]