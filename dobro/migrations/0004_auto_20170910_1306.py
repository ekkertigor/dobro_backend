# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dobro', '0003_auto_20170910_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='login',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
