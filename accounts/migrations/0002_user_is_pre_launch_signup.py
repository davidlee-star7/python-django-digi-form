# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_pre_launch_signup',
            field=models.BooleanField(default=False),
        ),
    ]
