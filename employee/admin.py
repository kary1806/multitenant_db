from django.contrib import admin

from employee import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = [
        "name",
    ]
