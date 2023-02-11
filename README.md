empA = Employee.objects.create(emp_id= 1001, emp_name='Employee A')

empB = Employee.objects.create(emp_id= 1002, emp_name='Employee B', manager=empA)

empC = Employee.objects.create(emp_id= 1003, emp_name='Employee C', manager=empB)

empD = Employee.objects.create(emp_id= 1004, emp_name='Employee D', manager=empA)

empE = Employee.objects.create(emp_id= 1005, emp_name='Employee E', manager=empB)

empF = Employee.objects.create(emp_id= 1006, emp_name='Employee F', manager=empC)
