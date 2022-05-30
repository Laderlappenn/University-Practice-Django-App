from django.forms import ModelForm
from django import forms
from .models import act, user

RELEVANCE_CHOICES = (
    (1, "Сантехника"),
    (2, "электрика"),
    (3, "строитель"),
    (4, "плотник"),
)

# class ActForm(forms.Form):
#     adress = forms.CharField(label='Точный адресс:Здание, помещение, этаж, кабинет/квартира.', max_length=100, widget=forms.TextInput(attrs={'class': 'formclass'}))
#     type = forms.ChoiceField(label='Тип заявки:',choices = RELEVANCE_CHOICES)
#     full_name = forms.CharField(label='ФИО',max_length=40, widget=forms.TextInput(attrs={'class': 'formclass'}))
#     phone_number = forms.CharField(label='Телефон',max_length=17, widget=forms.TextInput(attrs={'class': 'formclass'}))
#     act_text = forms.CharField(label='Описание',widget=forms.Textarea(attrs={'class': 'formclass'}))

class CreateUserForm(ModelForm):
    class Meta:
        model = user
        fields = '__all__'


class ActForm(ModelForm):
    class Meta:
        model = act
        fields = '__all__'

