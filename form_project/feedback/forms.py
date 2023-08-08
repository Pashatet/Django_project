from django import forms
from .models import Feedback

# первый способ подстроение модели под форму
# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=10, min_length=2, error_messages={
#         'max_length': 'слишком много символов',
#         'min_length': 'слишком мало символов',
#     })
#     lastname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':40}))
#     rating = forms.IntegerField(label='Рейтинг')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'lastname', 'feedback', 'rating']
        # передать все поля в форму
        fields = '__all__'
        # exclude = ['rating']
        labels = {
            'name': 'Имя',
            'lastname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': {'max_length': 'ой как много символов',
                     'min_length': 'ой как мало символов',
                     'required': 'Не должно быть пустым'
                     },
            'surname': {'max_length': 'ой как много символов',
                        'min_length': 'ой как мало символов',
                        'required': 'Не должно быть пустым'
                        },
            'feedback': {'max_length': 'ой как много символов',
                         'min_length': 'ой как мало символов',
                         'required': 'Не должно быть пустым'
                         }
        }