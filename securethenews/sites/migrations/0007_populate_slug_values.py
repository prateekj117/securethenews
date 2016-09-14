# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-13 05:11
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def gen_slugs_from_names(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    for site in Site.objects.all():
        site.slug = slugify(site.name)
        site.save()

class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_add_slug_field'),
    ]

    operations = [
        migrations.RunPython(
            gen_slugs_from_names,
            reverse_code=migrations.RunPython.noop
        ),
    ]
