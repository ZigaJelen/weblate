# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0009_auto_20180129_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='nplurals',
        ),
        migrations.RemoveField(
            model_name='language',
            name='plural_type',
        ),
        migrations.RemoveField(
            model_name='language',
            name='pluralequation',
        ),
    ]
