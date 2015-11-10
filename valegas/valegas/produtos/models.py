from django.db import models

# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome


class Produto(models.Model):
	IS_PROMOCAO_CHOICES = (('N', 'NÃO'),('S', 'SIM'),)
	descricao_simples = models.CharField(u'Descrição Reduzida',max_length=255)
	descricao_completa = models.CharField(u'Descrição Completa', max_length=255)
	resumo 			  = models.CharField(u'Resumo', max_length=255)
	valor_compra      = models.DecimalField(u'valor de compra R$', max_digits=5, decimal_places=2, help_text='Volor que foi comprado.');
	valor_venda       = models.DecimalField(u'valor de venda R$', max_digits=5, decimal_places=2, help_text='Volor que será vendido.');
	categoria         = models.ForeignKey(Categoria)
	estoque           = models.IntegerField()
	#foto              = models.ImageField(upload_to="images/prodthumbs/")
	is_promocao       = models.CharField(max_length=1, choices=IS_PROMOCAO_CHOICES)
	valor_promocao    = models.DecimalField(u'valor promocional R$', max_digits=5, decimal_places=2, help_text='Volor que será vendido quando for promocional.');

	def __str__(self):
		return self.descricao_simples

	def get_preco(self):
		if self.is_promocao == 'N':
			return self.valor_venda
		else:
			return self.valor_promocao