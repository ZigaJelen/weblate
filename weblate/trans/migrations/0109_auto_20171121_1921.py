# -*- coding: utf-8 -*-
# Generated by Django 1.11.5.dev20170816164241 on 2017-11-21 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0108_auto_20171121_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['priority', 'position'], 'permissions': (('save_translation', 'Can save translation'), ('save_template', 'Can save template'), ('review_translation', 'Can review translation'))},
        ),
    ]
