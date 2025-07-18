from django.urls import path
from first_drf_app import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = SimpleRouter()
router.register('company_model_viewset', views.CompanyModelViewset, 'company_model_viewset')
router.register('employees', views.EmployeeModelViewset, 'em')


urlpartterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('hello/', views.hello),
    path('company/', views.CompanyListAPIView.as_view()),
    path('company/<int:sina>/', views.CompanyDetail.as_view()),
    path('my_viewset/', views.MyFirstViewset.as_view(
        {"get": "hossein", "post": "sina"}
        )
    ),
    path('company_viewset/', views.CompanyListViewset.as_view(
        {"get": "list", "post": "create"}
        )
    ),
    path('company_viewset/<int:sina>', views.CompanyDetailViewset.as_view(
            {  
                "get": "retrieve",
                "put": 'update',
                "patch": 'partial_update',
                "delete": "destroy"
            }
        )
    )
]
urlpartterns = urlpartterns + router.urls

#asm:sina1234
# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjgzMzk5NiwiaWF0IjoxNzUyODI2Nzk2LCJqdGkiOiIxMjMzYjM0ZjNjOWU0NDg4ODNhNzFkNjkzOTBlZGNmNiIsInVzZXJfaWQiOjF9.M4iTSYSRLjtDiu5aQPFjW6G_mtnePz-ragZF43weZss",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyODI3Njk2LCJpYXQiOjE3NTI4MjY3OTYsImp0aSI6IjlkZThhODJmN2E4YzRkNmRhNzcyMGQ5ZGQ5NWE0YTQ5IiwidXNlcl9pZCI6MX0.KHg54pC0Jfa-lAqs-vEGCR_VpQFkfYutL9o-GLWzUmA"
# }

# {
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyODI3NzU4LCJpYXQiOjE3NTI4MjY3OTYsImp0aSI6Ijc2NzYxMThiMWU4YjQxZDFiMzQzOWQxNzY3YzU5NjdjIiwidXNlcl9pZCI6MX0.XR5OT6ej5bIkHAnbqXq0wsXIT0YDBuHQvk8YCcMo7pU",
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjgzNDA1OCwiaWF0IjoxNzUyODI2ODU4LCJqdGkiOiI0YTY0YzI4ZDFiYzY0MDZmOTY4MmEwZWUyNDllMDk4NCIsInVzZXJfaWQiOjF9.20cpbxwofglP9on073GOERyZTK--gInBmAjcw430y3Q"
# }