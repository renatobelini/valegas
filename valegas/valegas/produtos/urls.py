from django.conf.urls import include, url
from valegas.produtos.views import lista_produtos, novo_produto, editar_produto, lista_categorias, nova_categoria, editar_categoria

urlpatterns = [
	url(r'^lista-produtos/$', lista_produtos, name='lista_produtos'),
	url(r'^lista-categorias/$', lista_categorias, name='lista_categorias'),
	url(r'^novo-produto/$', novo_produto, name='novo_produto'),
	url(r'^editar-produto/(?P<id>\d+)$', editar_produto, name='editar_produto'),
	url(r'^nova-categoria/$', nova_categoria, name='nova_categoria'),
	url(r'^editar-categoria/(?P<id>\d+)$', editar_categoria, name='editar_categoria'),
]