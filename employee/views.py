from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from employee import models, serializers


class CreateEmployee(APIView):
    """
    Registrar un empleado
    """

    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = serializers.CreateEmployee(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        models.Employee.objects.get_or_create(name=valid_data["name"])
        return Response(
            {"result": "OK"},
            status=status.HTTP_200_OK,
        )


class EmployeeList(APIView):
    """
    Obtener las listas empleados
    """

    permission_classes = []

    def get(self, request, *args, **kwargs):
        employee_lists = models.Employee.objects.all()
        serializer = serializers.EmployeeList(employee_lists, many=True)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_200_OK,
        )
