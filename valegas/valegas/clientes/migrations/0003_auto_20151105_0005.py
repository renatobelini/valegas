# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20151104_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bairro',
            old_name='nome',
            new_name='nome_bairro',
        ),
    ]
