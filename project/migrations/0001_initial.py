# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('related_to', models.CharField(max_length=200, choices=[('school', 'School'), ('private', 'Private'), ('work', 'Work')])),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
