# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainbody', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexArticle',
            fields=[
                ('articlenumber', models.IntegerField(serialize=False, primary_key=True)),
                ('articlename', models.CharField(unique=True, max_length=20)),
                ('articletitle', models.CharField(max_length=50)),
                ('articlecontent', models.TextField()),
                ('contentlink', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'indexarticle',
            },
        ),
    ]
