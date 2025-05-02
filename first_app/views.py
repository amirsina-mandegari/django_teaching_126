from django.shortcuts import render

from django.http import HttpResponse

from first_app.forms import ContactForm


def hello_view(request):
    sina = {
        'username' : 'amirsina',
        'skills' : ['django', 'drf', 'python']
    }
    return render(request, 'greetings/home.html', sina)


def contact_view(request):
    form = ContactForm()

    return render(request, 'contact_page.html', {'form':form})