# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160602_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='file',
            new_name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]