# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-31 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_document', '0010_formdocumentlink_form_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdocumenttemplate',
            name='archived_on',
            field=models.DateTimeField(null=True),
        ),
    ]
