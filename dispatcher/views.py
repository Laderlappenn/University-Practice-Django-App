from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import CreateUserForm, ActForm
from .models import act


def home(request):
    return render (request, 'dispatcher/home.html',{})


def create(request):
    form_class = CreateUserForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    return render(request, 'dispatcher/create_user.html', {'form':form})


def act_page(request):
    form_class = ActForm

    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = ActForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect('http://127.0.0.1:8000/list/')
    else:
        form = ActForm()

    return render(request, 'dispatcher/act.html', {'form': form})


def act_list(request):
    acts = act.objects.all



    return render(request, 'dispatcher/act_list.html', {'acts':acts})
