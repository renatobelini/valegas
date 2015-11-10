# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('descricao_simples', models.CharField(verbose_name='Descrição Reduzida', max_length=255)),
                ('descricao_completa', models.CharField(verbose_name='Descrição Completa', max_length=255)),
                ('resumo', models.CharField(verbose_name='Resumo', max_length=255)),
                ('valor_compra', models.DecimalField(verbose_name='valor de compra R$', decimal_places=2, help_text='Volor que foi comprado.', max_digits=5)),
                ('valor_venda', models.DecimalField(verbose_name='valor de venda R$', decimal_places=2, help_text='Volor que será vendido.', max_digits=5)),
                ('estoque', models.IntegerField()),
                ('is_promocao', models.CharField(max_length=1, choices=[('N', 'NÃO'), ('S', 'SIM')])),
                ('valor_promocao', models.DecimalField(verbose_name='valor promocional R$', decimal_places=2, help_text='Volor que será vendido quando for promocional.', max_digits=5)),
                ('categoria', models.ForeignKey(to='produtos.Categoria')),
            ],
        ),
    ]
