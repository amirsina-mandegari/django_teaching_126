from django_filters import rest_framework as filters

from first_drf_app.models import Company


class CompanyFilter(filters.FilterSet):
    class Meta:
        model = Company
        fields = {
            'name': ['icontains', 'exact'],
            'manager_name': ['exact']
        }
