# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Texto', models.TextField()),
                ('Cadeira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.Cadeira')),
            ],
        ),
        migrations.AddField(
            model_name='subtema',
            name='Tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.Tema'),
        ),
    ]