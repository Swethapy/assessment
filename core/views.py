from django.shortcuts import render
from .models import Employee


def index(request):
    """
    API Endpoint: http://127.0.0.1:8000/core/index/
    This is a sample function based view which takes static data and display it in HTML Template
    """
    employees = {
        "emp_id": 1001,
        "emp_name": "Adam Smith",
        "manager_name": "Sean Marsh"
    }
    return render(request, "core/index.html", {"employees": employees})


def dashboard(request):
    """
    API Endpoint: http://127.0.0.1:8000/core/employees/
    This is a function-based view.
    This GET API Endpoint will return all the Employee objects/records from the DB
    and order them based on emp_id in an ascending order.
    These employees will be sent to the HTML Template to incorporate it using Jinja Templating Language
    """
    employees = Employee.objects.order_by('emp_id').all()
    context = {'employees': employees}
    return render(request, 'core/employees.html', context)
