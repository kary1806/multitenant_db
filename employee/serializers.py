from rest_framework import serializers

from employee import models


class CreateEmployee(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)


class EmployeeList(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ("id", "name", "date_created")
