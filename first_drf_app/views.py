from rest_framework.decorators import api_view
from rest_framework.response import Response

from first_drf_app.models import Company

@api_view()
def hello(request):
    return Response({"message": "hello from DRF!"})


@api_view(['GET', 'POST'])
def company(request):
    if request.method == "GET":
        company = Company.objects.all().values()
        return Response(list(company))
    
    elif request.method == "POST":
        company_obj = Company.objects.create(**request.data)
        return Response({'id': company_obj.id, 'name': company_obj.name})