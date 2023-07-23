from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def leo(request):
#     return HttpResponse('LEO')
#
#
# def aries(request):
#     return HttpResponse('aries')
#
#
# def taurus(request):
#     return HttpResponse('taurus')
signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_info_about_sign_zodiac(request, sign_of_zodiac: str):
    # description = signs.get(sign_of_zodiac)
    # первыйвариант привязать шаблон
    # response = render_to_string('horoscope/info_zodiac.html')
    # return HttpResponse(response)
    # второй вариант привязать шаблонc
    description = signs.get(sign_of_zodiac)
    data = {
        "signs": description
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)
    # if description:
    #     return HttpResponse(signs[sign_of_zodiac.lower()])
    # return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_of_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_of_zodiac: int):
    zodiacs = list(signs)
    if sign_of_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер знака зодиака - {sign_of_zodiac}")
    name_zodiac = zodiacs[sign_of_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def index(request):
    zodiacs = list(zodiac_element)
    context = {
        "zodiacs": signs
    }
    return render(request, 'horoscope/index.html', context=context)


def type_index(request):
    li_elements = ''
    for x in zodiac_element:
        li_elements += f'<li> <a href="{x}/"> {x.title()} </a> </li>'
    return HttpResponse(f'<ul>{li_elements}</ul>')


def type_horoscope(request, type_of_name: str):
    li_elements = ''
    for x in zodiac_element[type_of_name]:
        redirect_path = reverse('horoscope-name', args=[x])
        li_elements += f'<li> <a href="{redirect_path}"> {x.title()} </a> </li>'
    return HttpResponse(f'<ul>{li_elements}</ul>')


def get_my_date_converters(request, sign_of_zodiac):
    return HttpResponse(f'Вы передали месяц,число,год из 4-х символов - {sign_of_zodiac}')


def get_yyyy_converters(request, sign_of_zodiac):
    return HttpResponse(f'Вы передали число из 4-х символов - {sign_of_zodiac}')


def get_my_float_converters(request, sign_of_zodiac):
    return HttpResponse(f'Вы передали нецелое число - {sign_of_zodiac}')


def get_my_list_converters(request, sign_of_zodiac):
    return HttpResponse(f"{sign_of_zodiac}")


def get_my_upper_convertes(request, sign_of_zodiac):
    return HttpResponse(f"{sign_of_zodiac}")


people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]


def get_info_about_people(request):
    data = {
        "peoples": people
    }
    return render(request, 'horoscope/people.html', context=data)
