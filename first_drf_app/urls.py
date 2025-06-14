from django.urls import path
from first_drf_app import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register('company_model_viewset', views.CompanyModelViewset)


urlpartterns = [
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