# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-09 11:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
