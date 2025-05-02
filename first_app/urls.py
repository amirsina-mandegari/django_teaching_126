from django.urls import path

from first_app.views import hello_view, contact_view


urlpatterns = [
    path('hello/', hello_view),
    path('contact/', contact_view, name='contact')
]
