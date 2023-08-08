from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=10, min_length=2, error_messages={
        'max_length': 'слишком много символов',
        'min_length': 'слишком мало символов',
    })
    lastname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':40}))
    rating = forms.IntegerField(label='Рейтинг')