from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def home(request):
    template = loader.get_template('cti_final/main_page_template.html')
    return HttpResponse(template.render())