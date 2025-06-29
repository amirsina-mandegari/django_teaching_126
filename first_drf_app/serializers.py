from rest_framework import serializers
from first_drf_app.models import Company, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')


class CompanySerializer(serializers.ModelSerializer):
    age_in_days = serializers.SerializerMethodField()
    age_in_month = serializers.IntegerField(read_only=True)
    employees = EmployeeSerializer(many=True)
    
    class Meta:
        model = Company
        exclude = ('id',)

    def get_age_in_days(self, obj):
        return obj.age * 365


class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('id', 'employees')

    def validate_name(self, value):
        if 'company' in value:
            raise serializers.ValidationError('your name should not have company')
        return value
    
    def validate(self, attrs):
        name = attrs.get('name')
        manager_name = attrs.get('manager_name')
        if name == manager_name:
            raise serializers.ValidationError('name and manager name should not be same!')
        return super().validate(attrs)




class CompanyEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['email']