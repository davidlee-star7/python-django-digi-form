# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-01 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_auto_20160901_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_cents', models.IntegerField()),
                ('trial_days', models.SmallIntegerField(default=0, null=True)),
            ],
            options={
                'ordering': ('pricing__name',),
                'verbose_name': 'Plan pricing',
                'verbose_name_plural': 'Plans pricings',
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True)),
                ('recurring_type', models.CharField(choices=[('D', 'Day'), ('W', 'Week'), ('M', 'Month'), ('Y', 'Year')], default='M', max_length=1)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Pricing',
                'verbose_name_plural': 'Pricings',
            },
        ),
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ('name',), 'verbose_name': 'Plan', 'verbose_name_plural': 'Plans'},
        ),
        migrations.RenameField(
            model_name='plansubscription',
            old_name='price_cents',
            new_name='amount_cents',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='target_plans',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='price_cents',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='recurring_type',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='trial_days',
        ),
        migrations.RemoveField(
            model_name='plansubscription',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='plansubscription',
            name='name',
        ),
        migrations.RemoveField(
            model_name='plansubscription',
            name='recurring_type',
        ),
        migrations.RemoveField(
            model_name='plansubscription',
            name='trial_days',
        ),
        migrations.AddField(
            model_name='planpricing',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Plan'),
        ),
        migrations.AddField(
            model_name='planpricing',
            name='pricing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.Pricing'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='target_pricing_plan',
            field=models.ManyToManyField(blank=True, help_text='Leaving empty will make this coupon valid for all plans', to='billing.PlanPricing'),
        ),
        migrations.AddField(
            model_name='plansubscription',
            name='plan_pricing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.PlanPricing'),
        ),
    ]
