"""cti_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from . import views

from django.template import loader

urlpatterns = [
    #main page url
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),

    #connects to the formula urls and templates
    url(r'^formulas/', include('formulas.urls')),

    #connects to the flakes_game urls and templates
    url(r'^flakes/', include('flakes_game.urls'))
]
