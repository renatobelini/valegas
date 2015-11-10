from django import forms
from valegas.produtos.models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = ('descricao_simples', 'descricao_completa', 'resumo', 'valor_compra', 'valor_venda', 'categoria', 'estoque', 'is_promocao', 'valor_promocao')


class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ('nome',)