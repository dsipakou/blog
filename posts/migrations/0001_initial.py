# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('publish', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]