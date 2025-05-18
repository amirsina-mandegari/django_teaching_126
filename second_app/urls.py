from django.urls import path
from second_app import views


urlpatterns = [
    path('set_cookie/', views.set_color),
    path('get_color/', views.access_color),
    path('delete_cookie/', views.delete_cookie),
    path('add_to_cart/<int:item_id>/', views.add_to_cart),
    path('view_cart/', views.view_cart),
    path('empty_cart/', views.empty_cart),
    path('check_request/', views.check_request_user),
    path('check_request_user_template/', views.check_request_user_template),
    path('login/', views.custom_login, name='login_page'),
    path('logout/', views.custom_logout)
]
