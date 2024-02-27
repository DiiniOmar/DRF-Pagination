import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Pagination.settings')
import django
django.setup() 
from testApp.models import Employee
from faker import Faker
from random import randint

fake = Faker() 

def populate(n):
   
    for i in range(n):
        femp_number = randint(1001, 9999)
        femp_name = fake.name()
        femp_salary = randint(65000, 75000)
        femp_email = fake.email()
        femp_address = fake.city()
        emp_record = Employee.objects.get_or_create(emp_number=femp_number, emp_name=femp_name, emp_salary=femp_salary, emp_email=femp_email, emp_address=femp_address)

n = int(input("Enter number of records: "))
populate(n)
print(f'{n} Records inserted successfully')
