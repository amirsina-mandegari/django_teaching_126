from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from first_app.forms import ContactUsForm


def hello_view(request):
    sina = {
        'username' : 'amirsina',
        'skills' : ['django', 'drf', 'python']
    }
    return render(request, 'greetings/home.html', sina)

@permission_required('first_app.send_contact_us')
def contact_view(request):
    print(f"the method is:{request.method}")
    if request.method == 'POST':
        print(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, "thank you for your submission")
        else:
            messages.error(request, "you have error on your form")
        return HttpResponseRedirect(reverse('contact'))
    else:   
        form = ContactUsForm()
        return render(request, 'contact_us.html', {'form':form})