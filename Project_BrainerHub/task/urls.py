from django.urls import path
from .views import *

urlpatterns = [
    path('upload', upload_employee_data, name='upload_emp_data'),
    path('emp/<int:id>', get_employee_info),
    path('allemp', all_employee_info),


]