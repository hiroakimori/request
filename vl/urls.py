from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.req_list, name='req_list'),
    path('req_post/', views.req_post, name='req_post'),
    path('approve/<pk>/', views.approve, name='approve'),
]