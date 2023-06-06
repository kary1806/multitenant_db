from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions import models, serializers


class CreateTransaction(APIView):
    """
    Registrar una transaccion
    """

    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = serializers.CreateTransaction(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        models.Transaction.objects.get_or_create(employee_id=valid_data["employee_id"], amount=valid_data["amount"])
        return Response(
            {"result": "OK"},
            status=status.HTTP_200_OK,
        )


class TransactionList(APIView):
    """
    Obtener las listas transacciones
    """

    permission_classes = []

    def get(self, request, *args, **kwargs):
        employee_lists = models.Transaction.objects.all()
        serializer = serializers.TransactionList(employee_lists, many=True)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_200_OK,
        )
