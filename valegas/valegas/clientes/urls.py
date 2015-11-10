from django.conf.urls import include, url
from valegas.clientes.views import lista_clientes, novo_cliente, editar_cliente, novo_bairro

urlpatterns = [
	url(r'^lista-cliente/$', lista_clientes, name='lista_clientes'),
	url(r'^novo-cliente/$', novo_cliente, name='novo_cliente'),
	url(r'^editar-cliente/(?P<id>\d+)$', editar_cliente, name='editar_cliente'),
	url(r'^novo-bairro/$', novo_bairro, name='novo_bairro'),
]