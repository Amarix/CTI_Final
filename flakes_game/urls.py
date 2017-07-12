from django.conf.urls import url
from . import views
from django.template import loader
urlpatterns = [
    url(r'^$', views.flake_page, name='flake_page'),
]