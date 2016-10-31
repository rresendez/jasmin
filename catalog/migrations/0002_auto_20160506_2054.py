# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=6, default=None, choices=[('Male', 'Male'), ('Female', 'Female')], verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='media',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, default=None, choices=[('Search Engine', 'Search Engine'), ('Social Network', 'Social Network'), ('Advertisement', 'Advertisement'), ('Friend', 'Friend'), ('Other', 'Other')], verbose_name='Media'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='occupation',
            field=models.CharField(max_length=30, default=None, choices=[('Arts', 'Arts'), ('Architecture', 'Architecture'), ('Advertising', 'Advertising'), ('Accounting', 'Accounting'), ('Information Technology', 'Information Technology'), ('Clerical', 'Clerical'), ('Sales', 'Sales'), ('Other', 'Other')], verbose_name='Occupation'),
        ),
    ]
