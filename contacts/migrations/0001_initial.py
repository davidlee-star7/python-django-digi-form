# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-07 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw', models.CharField(blank=True, help_text='address line 1', max_length=200)),
                ('unit_no', models.CharField(blank=True, max_length=6)),
                ('street_number', models.CharField(blank=True, max_length=32)),
                ('street_name', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('suburb', models.CharField(blank=True, max_length=64)),
                ('state_province_code', models.CharField(blank=True, max_length=32)),
                ('postal_code', models.CharField(blank=True, max_length=32)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=90)),
                ('last_name', models.CharField(max_length=90)),
                ('middle_name', models.CharField(blank=True, max_length=90)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'M'), (1, 'F')])),
                ('mobile_number', models.CharField(blank=True, max_length=32)),
                ('email', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Person'),
        ),
    ]