from django.contrib import admin
from django.urls import path, include

from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<category_name_url>/', views.category, name='category'),
    path('goto/', views.track_url, name='track_url'),
    path('category/<category_name_url>/add_page/', views.add_page, name='add_page'),
    path('like_category/', views.like_category, name='like_category'),
    path('suggest_category/', views.suggest_category, name='suggest_category'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='user_logout'),
]
