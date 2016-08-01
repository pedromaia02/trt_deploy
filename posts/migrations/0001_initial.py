# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-29 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hidrometros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=45)),
                ('medicao_inicial', models.FloatField(blank=True, null=True)),
                ('medicao_final', models.FloatField(blank=True, null=True)),
                ('horario_ligamento', models.TimeField(blank=True, null=True)),
                ('horario_desligamento', models.TimeField(blank=True, null=True)),
                ('data', models.DateField()),
            ],
            options={
                'db_table': 'hidrometros',
            },
        ),
    ]
