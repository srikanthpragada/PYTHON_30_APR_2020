from django.contrib import admin
from django.urls import path
from . import views, ajax_views

urlpatterns = [
    path('about/', views.about),
    path('employees/', views.list_employees),
    path('addemp/', views.add_employee),
    path('update/', views.update_employee),
    path("ajax/", ajax_views.ajax_demo),
    path("message/", ajax_views.send_message),
]
