# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-28 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20180919_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('python', 'development'), ('ps', 'personal'), ('etc', 'etc')], default='python', max_length=2),
        ),
    ]