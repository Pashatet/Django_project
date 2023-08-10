from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import Feedback

# логика представлений на основе классов
from django.views import View
# если нам только нужно вывести шаблон можно воспользоваться TemplateView
from django.views.generic.base import TemplateView
# если нам только нужно вывести шаблон только с записями базы данных можно воспользоваться ListView
from django.views.generic import ListView, DetailView
# форма в которой реализовано для метода get and post
from django.views.generic.edit import FormView, CreateView, UpdateView
# Create your views here.

# class FeedBackView(View):
#     def get(self, request):
#         form = forms.FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = forms.FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})

# class FeedBackView(FormView):
#     # указываем какую фому нужно отобразить название класса без вызова
#     form_class = forms.FeedbackForm
#     # имя темплейта и у нас готов метод get
#     template_name = 'feedback/feedback.html'
#     # указываем куда должно быть перенаправление при успешной обработке формы
#     success_url = '/done'
#     # указываем что будем делать с данными с данном случае
#     # сама форма летит внутрь шаблона под именем form
#
#     # CreateView с помошью него мы можем избавиться от этого метода
#     def form_valid(self, form):
#         # Значения приходЯТ в cleaned_data и значения валидные
#         form.save()
#         return super().form_valid(form)
#


class FeedBackViewUpdate(UpdateView):
    model = Feedback
    form_class = forms.FeedbackForm
    # fields = '__all__' если это используем то мы не получаем ошибку при перезаписывании данных т.к данные то не пустые
    template_name = 'feedback/feedback.html'
    success_url = '/done'


class FeedBackView(CreateView):
    model = Feedback
    # form_class = forms.FeedbackForm
    # если мы не будем настраивать форму то мы не сможем настраивать labels и error_message
    fields = '__all__'
    template_name = 'feedback/feedback.html'
    success_url = '/done'

def index(request):
    if request.method == 'POST':
        # автоматом создаст обьект если он будет валидныйм
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # нам делать не нужно т.к у нас прямая связь с формой
            # feed = Feedback(
            #     name=form.cleaned_data['name'],
            #     lastname=form.cleaned_data['lastname'],
            #     feedback=form.cleaned_data['feedback'],
            #     rating=form.cleaned_data['rating'],
            # ).save()
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = forms.FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = forms.FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        if request.method == 'POST':
            form = forms.FeedbackForm(request.POST, instance=feed)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = forms.FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'form': form})

    # создание формы с помощью html
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     if len(name) == 0:
    #         return render(request, 'feedback/feedback.html', context={'got_error': True})
    #     print(name)
    #     return HttpResponseRedirect('/done')
    # return render(request, 'feedback/feedback.html', context={'got_error': False})


#     создание формы с помощью django form
#     if request.method == 'POST':
#         name = request.POST['name']
#         if len(name) == 0:
#             return render(request, 'feedback/feedback.html', context={'form': form})
#         print(name)
#         return HttpResponseRedirect('/done')
#     return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Ivanov I.I'
        context['date'] = '22.22.2222'
        return context


def done(request):
    return render(request, 'feedback/done.html')


# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#       можно добавить внутрь нашего context
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['all_feed'] = Feedback.objects.all()
#         return context

# нужем нам для отображения списка данных хранящихся в нашей модели
class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    # изначлаьно ListView кладет данные в objectlist
    model = Feedback
    # можно переопределить название переменной в которой буду храниться все записи
    # context_object_name = 'и тут свое название'

    # может отфильтровать данные
    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gt=1)
        return filter_qs

# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedback'] = Feedback.objects.get(id=kwargs['id_feedback'])
#         return context
#detailview нужен для реализации вывода информации о отдельной записи
class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    # описываем model чтобы django понимал с какой таблички брать данные
    model = Feedback
    # в html для получения данных мы обращаемся к имени нашей модели Feedback в нижнем регистре
#     еще можно в html обращаться object

