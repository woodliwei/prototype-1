# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-01-14 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('definition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('symbol', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cn_name', models.CharField(max_length=10)),
            ],
        ),
    ]
