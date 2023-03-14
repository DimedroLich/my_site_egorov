from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    response = render_to_string('blog/list_detail.html')
    return HttpResponse(response)

def about(request,name_post):
    context = {
        'text': name_post
    }
    return render(request,'blog/detail_by_name.html',context=context)

def about_by_num(request,number_post:int):
    context = {
        'num': number_post
    }
    return render(request, 'blog/detail_by_number.html',context=context)