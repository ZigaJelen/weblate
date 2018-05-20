# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 11:46
from __future__ import unicode_literals

from django.db import migrations


def migrate_plurals(apps, schema_editor):
    Plural = apps.get_model('lang', 'Plural')
    Language = apps.get_model('lang', 'Language')
    for lang in Language.objects.all():
        Plural.objects.get_or_create(
            source=0,
            language=lang,
            defaults={
                'number': lang.nplurals,
                'equation': lang.pluralequation,
                'type': lang.plural_type,
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0006_plural'),
    ]

    operations = [
        migrations.RunPython(migrate_plurals),
    ]
