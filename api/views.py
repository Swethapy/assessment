from rest_framework.generics import ListAPIView
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeList(ListAPIView):
    """
    API Endpoint: http://127.0.0.1:8000/api/employees/
    This is a class-based view inheriting from generic ListAPIView.
    This GET API Endpoint will return all the Employee objects/records from the DB
    and order them based on emp_id in an ascending order
    """
    queryset = Employee.objects.order_by('emp_id').all()
    serializer_class = EmployeeSerializer
