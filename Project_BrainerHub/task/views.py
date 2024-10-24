from django.shortcuts import render, get_object_or_404
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from .serializer import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Employee


@api_view(['GET', 'POST']) 
@csrf_exempt
def upload_employee_data(request):
    if request.method == 'GET':
        return render(request, 'task/upload_file.html') 
    
    if request.method == 'POST':
        file = request.FILES.get('file') 

        if not file:
            return Response('No file uploaded', status=HTTP_400_BAD_REQUEST)

        if file.name.endswith('.csv'):
            df = pd.read_csv(file) 
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return Response('Wrong file extension (upload format - csv/xlsx)', status=HTTP_400_BAD_REQUEST)

        for val, row in df.iterrows():
            employee_data = {
                'emp_id': row['EMPLOYEE_ID'],
                'first_name': row['FIRST_NAME'],
                'last_name': row['LAST_NAME'],
                'phone_number': row['PHONE_NUMBER'],
                'salary': row['SALARY'],
                'manager_id': row['MANAGER_ID'],
                'department_id': row['DEPARTMENT_ID'],
                'company_name': {'name_of_company': row['COMPANY_NAME']}
            }
            serializer = EmployeeSerializer(data=employee_data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            
        messgae = {'message': 'Employees data uploaded successfully'},
        return Response(messgae, status=HTTP_201_CREATED)


@api_view(['GET'])
def get_employee_info(request, id):
    employee = get_object_or_404(Employee, emp_id=id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def all_employee_info(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee,  many=True)
    return Response(serializer.data, status=HTTP_200_OK)