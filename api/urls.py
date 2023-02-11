from django.urls import path
from .views import EmployeeList

app_name = 'api'

urlpatterns = [
    # api/employees/
    path('employees/', EmployeeList.as_view(), name='employees'),
]
