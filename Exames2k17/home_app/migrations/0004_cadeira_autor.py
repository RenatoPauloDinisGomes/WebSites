# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_cadeira_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='autor',
            field=models.CharField(default='Renato Dinis', max_length=50),
        ),
    ]