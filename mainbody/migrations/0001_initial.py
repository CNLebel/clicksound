# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBottomPicture',
            fields=[
                ('imgnumber', models.IntegerField(serialize=False, primary_key=True)),
                ('imgname', models.CharField(unique=True, max_length=20)),
                ('contentlink', models.CharField(max_length=20)),
                ('images', models.ImageField(upload_to=b'aboutbottompicture')),
            ],
            options={
                'db_table': 'aboutbottompicture',
            },
        ),
        migrations.CreateModel(
            name='IndexPhotoLbum',
            fields=[
                ('imgnumber', models.IntegerField(serialize=False, primary_key=True)),
                ('imgname', models.CharField(unique=True, max_length=20)),
                ('imgtitle', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'indexphotolbum')),
            ],
            options={
                'db_table': 'indexphotolbum',
            },
        ),
    ]
