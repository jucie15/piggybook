# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0026_auto_20170714_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contents',
            options={'ordering': ['id'], 'verbose_name_plural': 'contents'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='congressman',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
        migrations.AlterField(
            model_name='congressmanemotion',
            name='congressman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='congressman',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='congressman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
    ]