from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from first_drf_app.models import Company
from first_drf_app.serializers import CompanySerializer, CreateCompanySerializer


@api_view()
def hello(request):
    return Response({"message": "hello from DRF!"})


class CompanyListAPIView(GenericAPIView):
    queryset = Company.objects.all()
    # serializer_class = CompanySerializer

    # def get_queryset(self):
    #     return Company.objects.filter(age__gt=10)
    
    def get_serializer_class(self):
        print('check for serializer!')
        if self.request.method == "POST":
            return CreateCompanySerializer
        return CompanySerializer

    def get(self, request, *args, **kwargs):
        companies = self.get_queryset()
        serializer = self.get_serializer(companies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class CompanyDetail(
    RetrieveUpdateDestroyAPIView
):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sina'
