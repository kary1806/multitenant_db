from django.db import models
from employee import models as employee_models


class Transaction(models.Model):
    employee = models.ForeignKey(employee_models.Employee, verbose_name="Employee", on_delete=models.PROTECT)
    reference = models.CharField(max_length=250)
    amount = models.IntegerField()
    date_created = models.DateTimeField("Fecha Creación", auto_now_add=True)
    date_updated = models.DateTimeField("Fecha Actualizado", auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"
