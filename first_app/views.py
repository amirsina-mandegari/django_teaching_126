from django.shortcuts import render

from django.http import HttpResponse

from first_app.models import BlogPost


def hello_view(request):
    sina = {
        'username' : 'amirsina',
        'skills' : ['django', 'drf', 'python']
    }
    return render(request, 'greetings/home.html', sina)
