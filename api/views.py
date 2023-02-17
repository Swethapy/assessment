from rest_framework import viewsets

from .models import Employee
from .serializers import ReadEmployeeSerializer, WriteEmployeeSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadEmployeeSerializer

        return WriteEmployeeSerializer

