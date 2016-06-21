# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0002_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurate',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'activo'), (2, 'eliminado')], default=1),
        ),
    ]