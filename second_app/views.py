from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from second_app.forms import LoginCustomForm, CustomUserCreationForm
from rest_framework_simplejwt.authentication import JWTAuthentication

def set_color(request):
    response = HttpResponse('set successfully')
    response.set_cookie('color', 'blue', max_age=3600)
    return response


def access_color(request):
    cookies = request.COOKIES
    print(cookies, type(cookies))
    color = request.COOKIES.get('color', 'orange')
    return HttpResponse(f'your preferred color is {color}')


def delete_cookie(request):
    response = HttpResponse('cookie delete successfully')
    response.delete_cookie('color')
    return response


def add_to_cart(request, item_id):
    cart = request.session.get('cart', [])
    cart.append(item_id)
    request.session['cart'] = cart
    return HttpResponse(f"current cart {cart}")


def view_cart(request):
    sessions = request.session
    print(sessions, type(sessions), sessions.__dict__)
    cart = request.session.get('cart', [])
    return HttpResponse(f"current cart {cart}")


def empty_cart(request):
    del request.session['cart']
    return HttpResponse("data deleted")


def check_request_user(request):
    user = request.user
    print(type(user), user.__dict__)
    return HttpResponse(
        f"user: {request.user} - {request.user.is_authenticated}"
    )


def check_request_user_template(request):
    return render(request, 'check_request_user.html')


def custom_login(request):
    if request.method == 'POST':
        form = LoginCustomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request,
                username=username,
                password=password
                )
            if user:
                login(request, user)
                context = {'form': form, 'custom_message': f'welcome {user.username}'}
            else:
                context = {'form': form, 'custom_message': 'wrong data!'}
        else:
            context = {'form': form, 'custom_message': 'wrong form!'}
        return render(request, 'custom_login.html', context=context)

    form = LoginCustomForm()
    context = {'form': form}
    return render(request, 'custom_login.html', context=context)


def custom_logout(request):
    logout(request)
    return redirect('login_page')


def custom_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('login_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'custom_signup.html', {'form': form})
