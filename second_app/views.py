from django.http import HttpResponse


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