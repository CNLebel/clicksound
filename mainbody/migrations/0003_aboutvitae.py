# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainbody', '0002_indexarticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutVitae',
            fields=[
                ('vitaenumber', models.IntegerField(serialize=False, primary_key=True)),
                ('vitaename', models.CharField(unique=True, max_length=20)),
                ('vitaetitle', models.CharField(max_length=50)),
                ('vitaeleft', models.TextField()),
                ('vitaeright', models.TextField()),
            ],
            options={
                'db_table': 'aboutvitae',
            },
        ),
    ]
