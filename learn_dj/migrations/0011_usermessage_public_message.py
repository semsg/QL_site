# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-13 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_dj', '0010_auto_20171213_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='public_message',
            field=models.BooleanField(default=False),
        ),
    ]
