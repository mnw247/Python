# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-29 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180629_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='postedon',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
