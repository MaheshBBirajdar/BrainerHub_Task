from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    company_name = CompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        company_data = validated_data.pop('company_name')
        company_name, created = Company.objects.get_or_create(name_of_company=company_data['name_of_company'])
        employee = Employee.objects.create(company_name=company_name, **validated_data)
        return employee
