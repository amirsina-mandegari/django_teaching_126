from django.urls import path
from first_drf_app import views

urlpartterns = [
    path('hello/', views.hello), 
    path('company/', views.CompanyListAPIView.as_view()),
    path('company/<int:pk>/', views.company_detail)
]