# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('param_table_for_customer', '0008_auto_20171017_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='server',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='param_table_for_customer.Server'),
        ),
    ]
