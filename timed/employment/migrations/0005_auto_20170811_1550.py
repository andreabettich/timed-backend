# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0004_auto_20170811_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absencecredit',
            name='absence_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absence_credits', to='employment.AbsenceType'),
        ),
    ]
