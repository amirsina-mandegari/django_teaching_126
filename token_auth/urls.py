from django.urls import path
from token_auth import views


urlpatterns = [
    path('create', views.AuthenticateToken.as_view())
]