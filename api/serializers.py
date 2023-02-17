from rest_framework import serializers
from .models import Employee


class ReadEmployeeSerializer(serializers.ModelSerializer):
    manager_name = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ('emp_id', 'emp_name', 'manager_name')
        read_only_fields = fields


class WriteEmployeeSerializer(serializers.ModelSerializer):
    manager_name = serializers.SlugRelatedField(slug_field="emp_name", allow_null=True, queryset=Employee.objects.all())

    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'manager_name']


class EmployeeSerializer(serializers.ModelSerializer):
    manager_name = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'manager_name']

