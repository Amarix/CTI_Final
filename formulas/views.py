from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


# Create your views here.
def index(request):
    template = loader.get_template('formulas/formulas_page_template.html')
    return HttpResponse(template.render())