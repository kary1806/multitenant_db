from django.urls import path

from transactions import views

urlpatterns = [
    path(
        "api/v1/create_transactions/",
        views.CreateTransaction.as_view(),
        name="create_transactions",
    ),
    path(
        "api/v1/list_transactions/",
        views.TransactionList.as_view(),
        name="list_transactions",
    ),
]
