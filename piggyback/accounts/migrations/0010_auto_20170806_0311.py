# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 18:11
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20170803_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[accounts.models.birth_validator], verbose_name='생년월일'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=16, null=True, unique=True, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(blank=True, choices=[('1', 'MALE'), ('2', 'FEMALE')], max_length=2, null=True, verbose_name='성별'),
        ),
    ]
