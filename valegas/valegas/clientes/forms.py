from django import forms
from valegas.clientes.models import Cliente, Bairro

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ('nome',
					'fone',
					'nome',
					'rg',
					'cpf',
					'fone',
					'logradouro',
					'tipo_logradouro',
					'cep',
					'numero',
					'ponto_referencia', 'bairro')



class BairroForm(forms.ModelForm):
	class Meta:
		model = Bairro
		fields = ('nome_bairro','cidade', 'uf')

