from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.BBLoginView.as_view(), name='login'),
    path('accounts/login/', views.BBLogoutView.as_view(), name='logout'),
    path('profile/',views.profile,name='profile'),
    #path('logout/', TemplateView.as_view(template_name="dispatcher/logout.html"), name='logout'),
    path('', views.home, name='create'),
    # path('create/', views.create, name='create'),
    path('act/',views.act_page_create, name='act'),
    path('list/',views.act_list, name='act_list'),
    re_path(r'^act/(?P<actid>\d+)/',views.act_page, name='act_page')
    ]