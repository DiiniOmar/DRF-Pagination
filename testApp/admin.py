from django.contrib import admin
from testApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display =  ['emp_number', 'emp_name', 'emp_salary', 'emp_email', 'emp_address']

admin.site.register(Employee, EmployeeAdmin)