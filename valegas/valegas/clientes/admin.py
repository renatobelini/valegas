from django.contrib import admin
from valegas.clientes.models import Cliente, Bairro

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome',
					'fone',
					'nome',
					'rg',
					'cpf',
					'fone',
					'logradouro',
					'tipo_logradouro',
					'cep',
					'numero',
					'latitude',
					'longtude',
					'ponto_referencia',
					'bairro')

	search_fields = ('nome',)


@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
	list_display = ('nome_bairro',	'cidade','uf',)

	search_fields = ('nome_bairro',)
