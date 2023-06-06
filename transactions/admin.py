from django.contrib import admin

from transactions import models


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "employee", "amount"]
    search_fields = [
        "employee__name",
    ]
