from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View



from .forms import  ActForm #CreateUserForm
from .models import Act


def home(request):
    return render (request, 'dispatcher/home.html',{})

class BBLoginView(LoginView):
    template_name = 'dispatcher/login.html'

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'dispatcher/logout.html'

@login_required
def profile(request):
    return render(request,'dispatcher/profile.html', {})


# def create(request):
#     form_class = CreateUserForm
#     # if request is not post, initialize an empty form
#     form = form_class(request.POST or None)
#
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#
#     return render(request, 'dispatcher/create_user.html', {'form':form})

@login_required
def act_page_create(request):
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

@login_required
def act_page(request, actid):

    queryset = Act.objects.get(id=actid)
    # return render(request, 'dispatcher/act_page.html', {'act': queryset})
    if request.user.id == queryset.user_id:
        return render(request, 'dispatcher/act_page.html', {'act':queryset})

    else:
        return render(request, 'dispatcher/no_access.html')

@login_required
def act_list(request):
    current_user = request.user

    queryset = Act.objects.filter(user_id=current_user)
    #act = Act.objects.get(pk=user)



    return render(request, 'dispatcher/act_list.html', {'acts':queryset})
