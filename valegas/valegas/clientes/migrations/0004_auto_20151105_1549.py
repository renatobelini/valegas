# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20151105_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='bairro',
            field=models.OneToOneField(to='clientes.Bairro'),
        ),
    ]
