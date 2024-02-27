from django.shortcuts import render
from testApp.models import Employee
from testApp.serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination



class myPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'mypage'
    page_size_query_param = 'num' # you can give the page number as num=15
    max_page_size = 15 # the maximum number you want display in the page 
class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = myPagination
