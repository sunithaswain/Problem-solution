# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-02 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem_statement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission_stats',
            name='challeges_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem_statement.Challeges'),
        ),
    ]