from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)

def about(request,name_post):
    return HttpResponse(f'Информация о посте {name_post}')

def about_by_num(request,number_post:int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')