# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('orig_img', models.ImageField(null=True, upload_to='test/')),
                ('face_img', models.ImageField(null=True, upload_to='test/')),
                ('has_face', models.BooleanField(default=False)),
                ('has_modi', models.BooleanField(default=False)),
                ('has_kejr', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrainImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='train/')),
                ('label', models.ForeignKey(to='face_rec.Label')),
            ],
        ),
    ]
