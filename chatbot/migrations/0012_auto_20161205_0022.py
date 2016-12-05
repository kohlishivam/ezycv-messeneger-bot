# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0011_auto_20161203_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_input',
            name='LinkedIn',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='city',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='contact',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='dob',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='emailid',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='fbid',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='greetings',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='name',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='objective_achievements',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='objective_line1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
    ]
