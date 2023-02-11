from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    manager_name = serializers.StringRelatedField(source='manager.emp_name', read_only=True)

    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'manager_name']
