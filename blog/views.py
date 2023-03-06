from django.shortcuts import render, HttpResponse
# Create your views here.


def posts(request):
    return HttpResponse('Все посты блога')

def about(request,name_post):
    return HttpResponse(f'Информация о посте {name_post}')