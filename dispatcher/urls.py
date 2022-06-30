from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.BBLoginView.as_view(), name='login'),
    path('accounts/login/', views.BBLogoutView.as_view(), name='logout'),
    path('profile/',views.profile,name='profile'),
    path('logout/', views.BBLogoutView.as_view(), name='logout'),
    path('', views.home, name='create'),
    # path('register/', views.register, name='create'),
    path('act/',views.act_page_create, name='act'),
    path('list/',views.act_list, name='act_list'),
    path('act/<int:pk>/edit/',views.act_edit_form, name='act-edit-form'),
    re_path(r'^act/(?P<actid>\d+)/$',views.act_page, name='act_page'),
    path('dispatcher/list',views.dispatcher_act_list,name='dispatcher-act-list'),
    re_path(r'^act/(?P<actid>\d+)/return/$', views.return_act, name='return-act'),
    re_path(r'^act/(?P<actid>\d+)/accept/$', views.accept_act, name='return-act'),
    path('employees/', views.employees_list, name='employees_list'),
    path('dispatcher/status/',views.act_status, name='act-status'),

    ]