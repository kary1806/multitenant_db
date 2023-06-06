from employee import serializers as employee_serializer
from rest_framework import serializers

from transactions import models


class CreateTransaction(serializers.Serializer):
    employee_id = serializers.CharField(max_length=255, required=True)
    amount = serializers.IntegerField(required=True)


class TransactionList(serializers.ModelSerializer):
    employee = employee_serializer.EmployeeList()

    class Meta:
        model = models.Transaction
        fields = ("id", "employee", "amount", "date_created")
