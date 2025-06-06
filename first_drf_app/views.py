from rest_framework.decorators import api_view
from rest_framework.response import Response

from first_drf_app.models import Company
from first_drf_app.serializers import CompanySerializer


@api_view()
def hello(request):
    return Response({"message": "hello from DRF!"})


@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == "GET":
        company = Company.objects.all().values()
        return Response(list(company))
    
    elif request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Company.objects.create(**serializer.data)
        return Response(serializer.data, status=201)


@api_view(['GET', 'PATCH', 'DELETE'])
def company_detail(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({'error': 'company not found'}, status=404)
    if request.method == "GET":
        return Response({'name': company.name, 'age': company.age})
    if request.method == 'PATCH':
        name = request.data.get('name')
        company.name = name
        company.save()
        return Response({"updated": True})
    if request.method == "DELETE":
        company.delete()
        return Response({'deleted':True})