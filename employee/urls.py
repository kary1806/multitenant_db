from django.urls import path

from employee import views

urlpatterns = [
    path(
        "api/v1/create_employee/",
        views.CreateEmployee.as_view(),
        name="create_employee",
    ),
    path(
        "api/v1/list_employee/",
        views.EmployeeList.as_view(),
        name="list_employee",
    ),
]
