from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from django.http import  QueryDict
from django.core.paginator import Paginator
from .forms import RegistrationForm, ActSetDateForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone

from .forms import  ActForm
from .models import Act, Account
from django.db.models import Q

def home(request):
    return render (request, 'dispatcher/home.html',{})

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("успешная регистрация"))
            return HttpResponseRedirect('http://127.0.0.1:8000/list/')
    else:
        form = RegistrationForm()

    return render(request, 'dispatcher/registration.html',{'form':form})


class BBLoginView(LoginView):
    template_name = 'dispatcher/login.html'

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'dispatcher/logout.html'

@login_required
def profile(request):
    return render(request,'dispatcher/profile.html', {})


@login_required
def act_page_create(request):
    form_class = ActForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = ActForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user.id
            form.instance.user_id = user
            form.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/list/')
    else:
        form = ActForm()

    return render(request, 'dispatcher/act.html', {'form': form, })

@login_required
def act_page(request, actid):

    queryset = get_object_or_404(Act, id=actid) #Act.objects.get(id=actid)
    if request.user.id == queryset.user_id or request.user.is_staff == 1:
        if request.method == 'GET':
            return render(request, 'dispatcher/act_page.html', {'act':queryset})
        elif request.method == 'PUT':
            data = QueryDict(request.body).dict()
            form = ActForm(data, instance=queryset)
            if form.is_valid():
                form.save()
                Act.objects.filter(id=actid).update(act_processing='Ожидание принятия заявки')
                return render(request,'dispatcher/details/act-detail.html', {'act':queryset})

            return render(request, 'dispatcher/forms/edit-act-form.html', {'form': form})

    else:
        return render(request, 'dispatcher/no_access.html')

def act_edit_form(request, pk):
    queryset = get_object_or_404(Act, pk=pk)
    form = ActForm(instance=queryset)
    return render(request,'dispatcher/forms/edit-act-form.html',{'act':queryset,'form':form})

def return_act(request, actid):
    if request.user.is_staff == 1:
        Act.objects.filter(id=actid).update(act_processing='Заявка возвращена')

        return render(request, 'dispatcher/details/return-detail.html')

def accept_act(request, actid):
    if request.user.is_staff == 1:
        Act.objects.filter(id=actid).update(act_processing='Заявки принята')
        return render(request, 'dispatcher/details/accept-detail.html')

def set_date(request, actid):
    if request.user.is_staff == 1:
        if request.method == 'GET':
            queryset = Act.objects.filter(id=actid).values_list('do_until', flat=True).first()

            form = ActSetDateForm()#instance=queryset
            return render(request, 'dispatcher/forms/date-form.html', {'form': form,'act':actid, 'date':queryset})
        if request.method == 'PUT':
            # optimize query
            queryset = get_object_or_404(Act, id=actid)
            data = QueryDict(request.body).dict()
            form = ActSetDateForm(data, instance=queryset)
            if form.is_valid():
                form.save()

        return render(request, 'dispatcher/details/accept-detail.html')


@login_required
def act_list(request):

    current_user = request.user
    queryset = Act.objects.filter(user_id=current_user)

    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dispatcher/act_list.html', {'acts':queryset, 'page_obj':page_obj})

@login_required
def dispatcher_act_list(request):

    if request.user.is_staff == 1:
        queryset = Act.objects.all().order_by('-date_updated')

        paginator = Paginator(queryset, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'dispatcher/act_list.html', {'acts':queryset, 'page_obj':page_obj})
    else:
        return render(request, 'dispatcher/no_access.html')

def act_status(request):
    status = request.GET.get('status')

    if status == 'all':
        queryset = Act.objects.all().order_by('-date_updated')
    elif status == 'completed':
        queryset = Act.objects.filter(completed=True)
    elif status == 'uncompleted':
        queryset = Act.objects.filter(completed=False)
    elif status == 'new':
        queryset = Act.objects.filter(act_processing='Ожидание принятия заявки')
    elif status == 'expired':
        now = timezone.localtime(timezone.now())
        queryset = Act.objects.filter(do_until__lt=now).exclude(do_until=None)

    return render(request,'dispatcher/details/act-status.html', {'status':queryset} )

@login_required
def employees_list(request):
    if request.user.is_staff == 1:
        queryset = Account.objects.filter(~Q(type='USER'))

        paginator = Paginator(queryset, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'dispatcher/employees_list.html', {'employees':queryset, 'page_obj':page_obj})
    else:
        return render(request, 'dispatcher/no_access.html')