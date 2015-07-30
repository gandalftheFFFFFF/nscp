# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_git_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterField(
            model_name='project',
            name='date_added',
            field=models.DateField(),
        ),
    ]
