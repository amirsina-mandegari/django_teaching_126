from django.urls import path
from second_app import views


urlpatterns = [
    path('set_cookie/', views.set_color),
    path('get_color/', views.access_color),
    path('delete_cookie/', views.delete_cookie)
]
