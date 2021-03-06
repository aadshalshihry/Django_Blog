# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_description',
            field=models.CharField(max_length=255, verbose_name='Category description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=50, verbose_name='Category Name'),
        ),
    ]
