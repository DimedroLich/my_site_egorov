from django.shortcuts import render, HttpResponse
# Create your views here.

def main(request):
    return HttpResponse('<h1>Главная страница</h1>')

def posts(request):
    return HttpResponse('Все посты блога')