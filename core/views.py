from django.shortcuts import render,HttpResponse

# Create your views here.

def hello(request, nome, n1, n2):
    return HttpResponse('<h1>Olá {}! Primeiro {}! Segundo{}!</h1>'.format(nome, n1, n2))
