from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from valegas.clientes.models import Cliente, Bairro
from valegas.clientes.forms import ClienteForm, BairroForm

# Create your views here.


def lista_clientes(request):
	clientes = Cliente.objects.all()
	return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def novo_cliente(request):
	debug = ''
	if request.method == 'POST':
		form_cliente = ClienteForm(request.POST)
		if form_cliente.is_valid():
			form_cliente.save()

			return redirect(reverse('clientes:lista_clientes'))
		else:
			print(form_cliente.errors)
	else:
		debug = 'Novo Cadastro'
		form_cliente = ClienteForm()
	return render(request, 'clientes/novo_cliente.html', {'form_cliente': form_cliente, 'debug':debug})



def novo_bairro(request):
	if request.method == 'POST':
		form_bairro = BairroForm(request.POST)
		if form_bairro.is_valid():
			form_bairro.save()
			return redirect(reverse('clientes:lista_clientes'))
		else:
			print(form_bairro.errors)
	else:
		form_bairro = BairroForm()
	return render(request, 'clientes/novo_bairro.html', {'form_bairro': form_bairro, 'request': request})

def editar_cliente(request, id):
	cliente = Cliente.objects.get(id=id)
	if request.method == 'POST':
		form_cliente = ClienteForm(request.POST, instance=cliente)
		if form_cliente.is_valid():
			form_cliente.save()
			return redirect(reverse('clientes:lista_clientes'))
		else:
			print(form_cliente.errors)
	else:
		form_cliente = ClienteForm(instance=cliente)
	return render(request, 'clientes/editar_cliente.html', {'form_cliente': form_cliente})

