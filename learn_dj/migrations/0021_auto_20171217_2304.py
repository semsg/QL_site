# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-17 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_dj', '0020_auto_20171217_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnew',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]