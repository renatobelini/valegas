"""valegas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
1. Add an import:  from blog import urls as blog_urls
2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from valegas.core import urls as core_urls
from valegas.clientes import urls as clientes_urls
from valegas.produtos import urls as produtos_urls

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include(core_urls, namespace='core')),
	url(r'^clientes/', include(clientes_urls, namespace='clientes')),
	url(r'^produtos/', include(produtos_urls, namespace='produtos')),
]
