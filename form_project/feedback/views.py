from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import Feedback


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = Feedback(
                name=form.cleaned_data['name'],
                lastname=form.cleaned_data['lastname'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating'],
            ).save()
            return HttpResponseRedirect('/done')
    else:
        form = forms.FeedbackForm()
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

def done(request):
    return render(request, 'feedback/done.html')
