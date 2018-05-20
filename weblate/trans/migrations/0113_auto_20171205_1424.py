# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0112_auto_20171129_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='translation',
            options={'ordering': ['language__name'], 'permissions': (('upload_translation', 'Can upload translation'), ('overwrite_translation', 'Can overwrite with translation upload'), ('author_translation', 'Can define author of translation upload'), ('commit_translation', 'Can force commiting of translation'), ('update_translation', 'Can update translation from VCS'), ('push_translation', 'Can push translations to remote VCS'), ('reset_translation', 'Can reset translations to match remote VCS'), ('mass_add_translation', 'Can mass add translation'), ('automatic_translation', 'Can do automatic translation'), ('use_mt', 'Can use machine translation'))},
        ),
        migrations.RemoveField(
            model_name='translation',
            name='lock_time',
        ),
        migrations.RemoveField(
            model_name='translation',
            name='lock_user',
        ),
    ]
