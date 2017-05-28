# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-14 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('number_available', models.IntegerField(default=0)),
            ],
        ),
    ]
