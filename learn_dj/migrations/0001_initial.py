# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-07 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text_01', models.TextField(blank=True)),
                ('code_01', models.TextField(blank=True)),
                ('text_02', models.TextField(blank=True)),
                ('code_02', models.TextField(blank=True)),
                ('text_03', models.TextField(blank=True)),
                ('code_03', models.TextField(blank=True)),
                ('text_04', models.TextField(blank=True)),
                ('code_04', models.TextField(blank=True)),
                ('text_05', models.TextField(blank=True)),
                ('code_05', models.TextField(blank=True)),
                ('text_06', models.TextField(blank=True)),
                ('code_06', models.TextField(blank=True)),
                ('text_07', models.TextField(blank=True)),
                ('code_07', models.TextField(blank=True)),
                ('text_08', models.TextField(blank=True)),
                ('code_08', models.TextField(blank=True)),
                ('text_09', models.TextField(blank=True)),
                ('code_09', models.TextField(blank=True)),
                ('text_010', models.TextField(blank=True)),
                ('code_010', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]