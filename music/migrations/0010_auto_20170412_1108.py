# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20170412_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='detailed_description',
            field=models.CharField(default=b'detailed desc', max_length=200),
        ),
    ]