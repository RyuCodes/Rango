from django.contrib import admin
from django.urls import path, include

from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #slug should pass category_name_url to the views.category
    path('category/<category_name_url>/', views.category, name='category'),
]
