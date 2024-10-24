from django.db import models


class Company(models.Model):
    name_of_company = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_company


class Employee(models.Model):
    company_name = models.ForeignKey(Company, related_name='emp', on_delete=models.CASCADE)
    emp_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    salary =  models.FloatField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


