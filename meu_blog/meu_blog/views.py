from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Django</h1><h3>Hello EATI 2016</h3>')

def template(request):
    return render(request, 'template.html',{})