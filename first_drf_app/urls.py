from django.urls import path
from first_drf_app import views

urlpartterns = [
    path('hello/', views.hello)
]