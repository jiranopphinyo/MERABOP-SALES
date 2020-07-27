from django.urls import path
from HUMANRESOURCE.views_employee import *

app_name = "HUMANRESOURCE"
urlpatterns = [
    # EMPLOYEE
    path('employee/list/', employee_list, name="employee_list"),
    path('employee/detail/<str:id>/', employee_detail, name="employee_detail"),
    path('employee/create/', employee_create, name="employee_create"),
    path('employee/update/<str:id>/', employee_update, name="employee_update"),
    # EMPLOYEE PERSONAL
    path('employee/personal/create/<str:id>/', employee_personal_create, name="employee_personal_create"),
    path('employee/personal/update/<str:id>/', employee_personal_update, name="employee_personal_update"),
    # EMPLOYEE ADDRESS
    path('employee/address/create/<str:id>/', employee_address_create, name="employee_address_create"),
    path('employee/address/update/<str:id>/', employee_address_update, name="employee_address_update"),
]
