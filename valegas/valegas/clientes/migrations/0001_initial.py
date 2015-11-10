# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=12)),
                ('cpf', models.CharField(max_length=12)),
                ('fone', models.CharField(max_length=12)),
                ('logradouro', models.CharField(max_length=100)),
                ('tipo_logradouro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=12)),
                ('numero', models.CharField(max_length=12)),
                ('latitude', models.CharField(max_length=50)),
                ('longtude', models.CharField(max_length=50)),
                ('ponto_referencia', models.CharField(max_length=100)),
                ('bairro', models.ForeignKey(to='clientes.Bairro')),
            ],
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=models.ForeignKey(to='clientes.Cidade'),
        ),
    ]
