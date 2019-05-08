# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-08 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_category',
        ),
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ManyToManyField(to='insta.Category'),
        ),
    ]
