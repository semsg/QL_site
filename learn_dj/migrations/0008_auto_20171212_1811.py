# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-12 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_dj', '0007_goodmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodmessage',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='goodmessage',
            name='date_of_note',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='goodmessage',
            name='user_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
