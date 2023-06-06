from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField("Fecha Creación", auto_now_add=True)
    date_updated = models.DateTimeField("Fecha Actualizado", auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
