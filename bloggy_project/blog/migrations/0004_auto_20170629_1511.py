# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-29 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
