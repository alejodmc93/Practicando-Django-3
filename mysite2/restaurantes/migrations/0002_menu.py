# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plato', models.CharField(max_length=100)),
                ('restaurate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantes.Restaurate')),
            ],
        ),
    ]
