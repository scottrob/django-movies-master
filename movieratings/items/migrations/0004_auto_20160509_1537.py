# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20160509_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_1',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_10',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_11',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_12',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_13',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_14',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_15',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_16',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_17',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_18',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_19',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_2',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_20',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_3',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_4',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_5',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_6',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_7',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_8',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_9',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.IntegerField(default=0),
        ),
    ]
