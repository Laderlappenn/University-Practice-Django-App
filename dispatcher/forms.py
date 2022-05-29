from django import forms

RELEVANCE_CHOICES = (
    (1, "Сантехника"),
    (2, "электрика"),
    (3, "строитель"),
    (4, "плотник"),
)

class ActForm(forms.Form):
    building = forms.CharField(label='Здание, помещение:', max_length=100, widget=forms.TextInput(attrs={'class': 'formclass'}))
    adress = forms.CharField(label='Этаж, Кабинет, Квартира:', max_length=100, widget=forms.TextInput(attrs={'class': 'formclass'}))
    type = forms.ChoiceField(label='Тип заявки:',choices = RELEVANCE_CHOICES)
    full_name = forms.CharField(label='ФИО заявителя', widget=forms.TextInput(attrs={'class': 'formclass'}))
    number = forms.CharField(label='Номер', max_length=12, widget=forms.TextInput(attrs={'class': 'formclass'}))
    act_text = forms.CharField(label='Описание',widget=forms.Textarea(attrs={'class': 'formclass'}))


