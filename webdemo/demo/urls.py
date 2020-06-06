from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/',  views.about),
    path('employees/',  views.list_employees),
    path('addemp/',  views.add_employee),
]
