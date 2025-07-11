from django.urls import path
from token_auth import views


urlpatterns = [
    path('create', views.AuthenticateTokenAPIView.as_view()),
    path('logout', views.TokenDestroyAPIView.as_view)
]