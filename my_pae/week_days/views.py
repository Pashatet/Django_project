from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def get_info_greeting(request):
    return render(request, 'week_days/greeting.html')
# Create your views here.
def monday(responce):
    return HttpResponse('''<!DOCTYPE html>
                            <html>
                            <head>
                                <title>Пример таблицы HTML</title>
                            </head>
                            <body>
                                <table>
                                    <tr>
                                        <th>Список дел на понеделтние</th>
                                    </tr>
                                    <tr>
                                        <td>Бегит</td>
                            
                                    </tr>
                                    <tr>
                                        <td>Прес качат</td>
                                    </tr>
                                </table>
                            </body>
                            </html>
                            ''')


def tuesday(responce):
    return HttpResponse('''<!DOCTYPE html>
                            <html>
                            <head>
                                <title>Пример таблицы HTML</title>
                            </head>
                            <body>
                                <table>
                                    <tr>
                                        <th>Список дел на вторник</th>
                                    </tr>
                                    <tr>
                                        <td>Атжимуния</td>
                                    </tr>
                                    <tr>
                                        <td>Турнех</td>
                                    </tr>
                                </table>
                            </body>
                            </html>
                            ''')


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_info_about_week_days(responce, day_of_week):
    if day_of_week in days:
        return HttpResponse(day_of_week)
    return HttpResponseNotFound(f'такого дня нет - {day_of_week}')


def get_info_about_week_number_days(responce, day_of_week):
    numbers_days = list(days)
    if day_of_week > len(numbers_days) or day_of_week == 0:
        return HttpResponseNotFound(f"Неправильный порядковый номер дня недели - {day_of_week}")
    day_of_week = numbers_days[day_of_week - 1]
    redirect_url = reverse("day-of-week", args=[day_of_week])
    return HttpResponseRedirect(redirect_url)
