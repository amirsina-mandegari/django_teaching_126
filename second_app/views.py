from django.http import HttpResponse
from django.shortcuts import render


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
