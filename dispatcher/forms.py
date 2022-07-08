from django.forms import ModelForm
from .models import Act, Account
from django import forms
from django.contrib.auth.forms import UserCreationForm
# RELEVANCE_CHOICES = (
#     (1, "Сантехника"),
#     (2, "электрика"),
#     (3, "строитель"),
#     (4, "плотник"),
# )

# class ActForm(forms.Form):
#     adress = forms.CharField(label='Точный адресс:Здание, помещение, этаж, кабинет/квартира.', max_length=100, widget=forms.TextInput(attrs={'class': 'formclass'}))
#     type = forms.ChoiceField(label='Тип заявки:',choices = RELEVANCE_CHOICES)
#     full_name = forms.CharField(label='ФИО',max_length=40, widget=forms.TextInput(attrs={'class': 'formclass'}))
#     phone_number = forms.CharField(label='Телефон',max_length=17, widget=forms.TextInput(attrs={'class': 'formclass'}))
#     act_text = forms.CharField(label='Описание',widget=forms.Textarea(attrs={'class': 'formclass'}))

# class CreateUserForm(ModelForm):
#     class Meta:
#         model = auth_user
#         fields = '__all__'

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2',)

class ActForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'special'})
        self.fields['adress'].widget.attrs.update({'class': 'special'})
        self.fields['act_type'].widget.attrs.update({'class': 'special'})
        self.fields['text'].widget.attrs.update({'class': 'special'})
        self.fields['image'].widget.attrs.update({'class': 'special'})

    image = forms.ImageField(required = False)
    file = forms.FileField(required = False)

    class Meta:
        model = Act
        fields = '__all__'
        exclude = ('act_processing', 'do_until', 'user')


class ActSetDateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['do_until'].widget.attrs.update({'class': 'special'})

    class Meta:
        model = Act
        fields = ('do_until',)
        widgets = {
            'do_until': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# class ActSearch(forms.Form):
#     search = forms.CharField(label='Поиск', max_length=100)

