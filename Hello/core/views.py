from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, nacionalidade):
    return HttpResponse("<h1>Hello {} de {} anos, nacionalidade: {}</h1>".format(nome, idade, nacionalidade))