from django.shortcuts import render

from django.http import HttpResponse

from first_app.forms import ContactUsForm


def hello_view(request):
    sina = {
        'username' : 'amirsina',
        'skills' : ['django', 'drf', 'python']
    }
    return render(request, 'greetings/home.html', sina)


def contact_view(request):
    form = ContactUsForm()

    return render(request, 'contact_us.html', {'form':form})