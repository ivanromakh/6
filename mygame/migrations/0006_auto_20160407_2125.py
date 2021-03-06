# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygame', '0005_auto_20160407_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('strength', models.IntegerField(default=2)),
                ('intellegent', models.IntegerField(default=2)),
                ('swiftness', models.IntegerField(default=2)),
                ('diplonacy', models.IntegerField(default=2)),
                ('militant', models.IntegerField(default=2)),
                ('my_image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='Characters',
        ),
    ]
