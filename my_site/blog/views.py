from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return HttpResponse('Все посты блога')


def get_info_about_post(request, name_post):
    data = {
        'discription_post_name': name_post
    }
    return render(request, 'blog/detail_by_nam.html', context=data)


def det_info_about_post_number(request, number_post):
    data = {
        'discription_post_number': number_post
    }
    return render(request, 'blog/detail_by_number.html', context=data)
