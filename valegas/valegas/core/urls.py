from django.conf.urls import include, url
from valegas.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]