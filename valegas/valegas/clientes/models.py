from django.db import models

# Create your models here.

class Bairro(models.Model):
	nome_bairro   = models.CharField(max_length=100)
	cidade = models.CharField(max_length=100)
	
	ESTADO_CHOICES = (
	    ('AC', 'Acre'), 
	    ('AL', 'Alagoas'),
	    ('AP', 'Amapá'),
	    ('BA', 'Bahia'),
	    ('CE', 'Ceará'),
	    ('DF', 'Distrito Federal'),
	    ('ES', 'Espírito Santo'),
	    ('GO', 'Goiás'),
	    ('MA', 'Maranão'),
	    ('MG', 'Minas Gerais'),
	    ('MS', 'Mato Grosso do Sul'),
	    ('MT', 'Mato Grosso'),
	    ('PA', 'Pará'),
	    ('PB', 'Paraíba'),
	    ('PE', 'Pernanbuco'),
	    ('PI', 'Piauí'),
	    ('PR', 'Paraná'),
	    ('RJ', 'Rio de Janeiro'),
	    ('RN', 'Rio Grande do Norte'),
	    ('RO', 'Rondônia'),
	    ('RR', 'Roraima'),
	    ('RS', 'Rio Grande do Sul'),
	    ('SC', 'Santa Catarina'),
	    ('SE', 'Sergipe'),
	    ('SP', 'São Paulo'),
	    ('TO', 'Tocantins')
	)
	uf = models.CharField(max_length=2, choices=ESTADO_CHOICES)
	
	def __str__(self):
		return self.nome_bairro

class Cliente(models.Model):
	nome      = models.CharField(max_length=100)
	rg        = models.CharField(max_length=12)
	cpf       = models.CharField(max_length=12)
	fone      = models.CharField(max_length=12)
	logradouro      = models.CharField(max_length=100)
	tipo_logradouro = models.CharField(max_length=50)
	cep       = models.CharField(max_length=12)
	numero    = models.CharField(max_length=12)
	latitude  = models.CharField(max_length=50)
	longtude  = models.CharField(max_length=50)
	ponto_referencia  = models.CharField(max_length=100)
	#bairro    = models.OneToOneField(Bairro)
	bairro = models.ForeignKey(Bairro)



	def __str__(self):
		return self.nome

