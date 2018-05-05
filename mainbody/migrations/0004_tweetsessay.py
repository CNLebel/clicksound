# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainbody', '0003_aboutvitae'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetsEssay',
            fields=[
                ('essaynumber', models.IntegerField(serialize=False, primary_key=True)),
                ('essayname', models.CharField(unique=True, max_length=20)),
                ('essaytitle', models.CharField(max_length=50)),
                ('essaycontent', models.TextField()),
                ('essayimages', models.ImageField(upload_to=b'twwwtsessay')),
                ('imagetitle', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tweetsessay',
            },
        ),
    ]
