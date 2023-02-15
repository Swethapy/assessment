Create a new empty folder on your system and clone this repository in that folder.

 - git clone https://github.com/Swethapy/assessment.git

Then you should create a virtual environment in that folder. There are many ways to create a virtual environment such as - 

 - python -m venv venv

To activate the virtual environment you just created run the following command (in Windows)
 - .\venv\Scripts\activate

Then you can install all the required packages/dependencies for this project to run from requirements.txt file as -
 - pip install -r requirements.txt

Now, everything is in place. (shared the sqlite sample database with some sample data to play around with)

You can just run the local development server -
 - python manage.py runserver

Now development server should be running at this address on your local -
 - http://127.0.0.1:8000/

added 2-3 endpoints in the web application along with one rest endpoint.

1. http://127.0.0.1:8000/admin/api/employee/

This URL will take you to the Admin portal of the web application where you can manually enter the Employee and Manager data to play around with.

2. http://127.0.0.1:8000/core/employees/

This URL will take you to the Employees Dashboard page where we have shown the Employee-Manager hierarchy in a HTML table format.

4. http://127.0.0.1:8000/api/employees/

This API Endpoint returns the response with Employee and Managers are stored in a single JSON object.

Sample Response:
    [
        {
            "emp_id": 1001,
            "emp_name": "Employee A"
        },
        {
            "emp_id": 1002,
            "emp_name": "Employee B",
            "manager_name": "Employee A"
        },
        {
            "emp_id": 1003,
            "emp_name": "Employee C",
            "manager_name": "Employee B"
        },
        {
            "emp_id": 1004,
            "emp_name": "Employee D",
            "manager_name": "Employee A"
        },
        {
            "emp_id": 1005,
            "emp_name": "Employee E",
            "manager_name": "Employee B"
        },
        {
            "emp_id": 1006,
            "emp_name": "Employee F",
            "manager_name": "Employee C"
        }

----

*Commands used to insert some data through Django Shell*
empA = Employee.objects.create(emp_id= 1001, emp_name='Employee A')
empB = Employee.objects.create(emp_id= 1002, emp_name='Employee B', manager=empA)
empC = Employee.objects.create(emp_id= 1003, emp_name='Employee C', manager=empB)
empD = Employee.objects.create(emp_id= 1004, emp_name='Employee D', manager=empA)
empE = Employee.objects.create(emp_id= 1005, emp_name='Employee E', manager=empB)
empF = Employee.objects.create(emp_id= 1006, emp_name='Employee F', manager=empC)
