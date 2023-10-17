from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        queryset = Employee.objects.all()
        work_status = self.request.query_params.get('work_status')
        if work_status:
            queryset = queryset.filter(work_status=work_status)
        return queryset



