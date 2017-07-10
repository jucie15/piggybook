# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20170705_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardcomment',
            name='feedback',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_comment_set', to='board.Feedback'),
        ),
    ]
