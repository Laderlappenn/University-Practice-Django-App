from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='create'),
    # path('create/', views.create, name='create'),
    path('act/',views.act_page, name='act'),
    path('list/',views.act_list, name='act_list')
    ]