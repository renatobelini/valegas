from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from valegas.produtos.models import Produto, Categoria
from valegas.produtos.forms import ProdutoForm, CategoriaForm

# Create your views here.


def lista_categorias(request):
	categorias = Categoria.objects.all()
	return render(request, 'produtos/lista_categorias.html', {'categorias': categorias})

def lista_produtos(request):
	produtos = Produto.objects.all()
	return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def novo_produto(request):
	debug = ''
	if request.method == 'POST':
		debug = 'requição POST'
		form_produto = ProdutoForm(request.POST)
		
		if form_produto.is_valid():
			
			form_produto.save()
			return redirect(reverse('produtos:lista_produtos'))
		else:
			print(form_produto.errors)
	else:
		debug = 'Novo Cadastro'
		form_produto = ProdutoForm()
	return render(request, 'produtos/novo_produto.html', {'form_produto': form_produto, 'debug':debug})

def editar_produto(request, id):
	produto = Produto.objects.get(id=id)
	if request.method == 'POST':
		form_produto = ProdutoForm(request.POST, instance=produto)
		if form_produto.is_valid():
			form_produto.save()
			return redirect(reverse('produtos:lista_produtos'))
		else:
			print(form_produto.errors)
	else:
		form_produto = ProdutoForm(instance=produto)
	return render(request, 'produtos/editar_produto.html', {'form_produto': form_produto})


def nova_categoria(request):	
	if request.method == 'POST':		
		form_categoria = CategoriaForm(request.POST)
		if form_categoria.is_valid():
			form_categoria.save()
			return redirect(reverse('produtos:lista_categorias'))
		else:
			print(form_categoria.errors)
	else:
		form_categoria = CategoriaForm()
	return render(request, 'produtos/manter_categoria.html', {'form_categoria': form_categoria})

def editar_categoria(request, id):
	categoria = Categoria.objects.get(id=id)
	if request.method == 'POST':
		form_categoria = CategoriaForm(request.POST, instance=categoria)
		if form_categoria.is_valid():
			form_categoria.save()
			return redirect(reverse('produtos:lista_categorias'))
		else:
			print(form_categoria.errors)
	else:
		form_categoria = CategoriaForm(instance=categoria)
	return render(request, 'produtos/editar_categoria.html', {'form_categoria': form_categoria})	