# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieGraphs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hollywood',
            old_name='actors',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='hollywood',
            old_name='directors',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='hollywood',
            old_name='producers',
            new_name='producer',
        ),
    ]
