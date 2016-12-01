# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0009_auto_20161029_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='eresume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('mobile', models.IntegerField(max_length=100, null=True)),
                ('elaborate', models.CharField(max_length=1000)),
                ('fblink', models.URLField(max_length=1000)),
                ('description', models.CharField(max_length=10000)),
                ('emailid', models.EmailField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=250)),
                ('twitterlink', models.CharField(max_length=250)),
                ('work1', models.CharField(max_length=11250)),
                ('work2', models.CharField(max_length=250)),
                ('work3', models.CharField(max_length=250)),
                ('work4', models.CharField(max_length=250)),
                ('cvlink', models.CharField(max_length=250)),
                ('fbid', models.CharField(max_length=250)),
                ('i', models.CharField(default=b'0', max_length=250)),
                ('j', models.CharField(default=b'1', max_length=250)),
                ('field', models.CharField(default=b' ', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='event',
        ),
    ]
