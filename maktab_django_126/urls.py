"""
URL configuration for maktab_django_126 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from first_app.urls import urlpatterns as first_app_urls
from second_app.urls import urlpatterns as second_app_urls 
from first_drf_app.urls import urlpartterns as first_drf_app_urls
from token_auth.urls import urlpatterns as token_auth_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="maktab django 126",
        default_version='v1',
        description="our very first drf swagger on maktab django 126"
    ),
    public=True,
    permission_classes=[AllowAny]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include(first_app_urls)),
    path('second_app/', include(second_app_urls)),
    path('first_drf_app/', include(first_drf_app_urls)),
    path('login/', auth_view.LoginView.as_view()),
    path('token/', include(token_auth_urls)),
    path('swagger/', schema_view.with_ui(), name='schema-swagger-ui')
]
