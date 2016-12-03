# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0010_auto_20161201_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresume',
            name='cvlink',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='description',
            field=models.CharField(default=b'NULL', max_length=10000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='elaborate',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='emailid',
            field=models.EmailField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='fbid',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='fblink',
            field=models.URLField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='location',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='twitterlink',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work1',
            field=models.CharField(default=b'NULL', max_length=11250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work2',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work3',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work4',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
    ]
