from rest_framework.decorators import api_view, action
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
from first_drf_app.models import Company, Employee
from first_drf_app.serializers import CompanySerializer, EmployeeSerializer, CreateCompanySerializer, CompanyEmailSerializer
from first_drf_app.permissions import CustomIsAuthenticated

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

@api_view()
def hello(request):
    return Response({"message": "hello from DRF!"})


class CompanyListAPIView(GenericAPIView):
    queryset = Company.objects.all()
    permission_classes=[CustomIsAuthenticated]
    # serializer_class = CompanySerializer

    # def get_queryset(self):
    #     return Company.objects.filter(age__gt=10)
    
    def get_serializer_class(self):
        print('check for serializer!')
        if self.request.method == "POST":
            return CreateCompanySerializer
        return CompanySerializer

    def get(self, request, *args, **kwargs):
        print("enter api")
        companies = self.get_queryset()
        serializer = self.get_serializer(companies, many=True)
        print("exit api")
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


class MyFirstViewset(viewsets.ViewSet):
    def hossein(self, request):
        return Response({"message": "get list"})
    
    def sina(self, request):
        return Response({"message": "Post request"})


class CompanyListViewset(viewsets.GenericViewSet):
    queryset = Company.objects.all()
    # serializer_class = CompanySerializer

    # def get_queryset(self):
    #     return Company.objects.filter(age__gt=10)
    
    def get_serializer_class(self):
        print('check for serializer!')
        if self.request.method == "POST":
            return CreateCompanySerializer
        return CompanySerializer

    def list(self, request, *args, **kwargs):
        companies = self.get_queryset()
        serializer = self.get_serializer(companies, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class CompanyDetailViewset(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sina'


class CompanyModelViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = "id"

    def get_serializer_class(self):
        if self.action == "email_list":
            return CompanyEmailSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["GET"])
    def email(self, request, id):
        obj = self.get_object()
        return Response({"email":obj.email})
    

    @action(detail=False, url_path='emails', )
    def email_list(self, request):
        ser = self.get_serializer(self.get_queryset(), many=True)
        return Response(ser.data)

class EmployeeModelViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()