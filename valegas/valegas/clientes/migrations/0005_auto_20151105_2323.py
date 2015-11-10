# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20151105_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='bairro',
            field=models.ForeignKey(to='clientes.Bairro'),
        ),
    ]
