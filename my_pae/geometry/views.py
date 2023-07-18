from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

def get_info_about_rectangle_area(request, width, height):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_info_about_rectangle_area2(request, width, height):
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')
    if 'get_' in request.path_info:
        return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_info_about_square_area(request, width):
    return HttpResponse(f'Площадь квадрата размером {width} равна {pow(width, 2)}')


def get_info_about_circle_area(request, radius):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {pow(radius, 2) * 3.14}')
