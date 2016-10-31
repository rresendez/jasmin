# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('fname', models.CharField(verbose_name='First Name', max_length=30)),
                ('lname', models.CharField(verbose_name='Last Name', max_length=30)),
                ('email', models.EmailField(primary_key=True, verbose_name='Email', serialize=False, max_length=254)),
                ('phoneNumber', models.CharField(verbose_name='phoneNumber', max_length=12)),
                ('gender', models.CharField(verbose_name='Gender', max_length=6)),
                ('occupation', models.CharField(verbose_name='Occupation', max_length=30)),
                ('media', models.CharField(verbose_name='Media', max_length=200)),
                ('comments', models.CharField(null=True, verbose_name='Comments', blank=True, max_length=200)),
                ('password', models.CharField(verbose_name='Password', help_text='Please use at least one uppercase and a number', max_length=100)),
                ('registeredDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
