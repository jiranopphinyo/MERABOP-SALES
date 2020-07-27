from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

### HUMANRESOURCE:: ALL
from HUMANRESOURCE.models import *

#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class EmployeeAdmin(admin.ModelAdmin):
    search_fields   = ['user__user', 'first_name', 'last_name']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'user',
        'first_name',
        'last_name',
        'created_at',
        'updated_at',
    ]

@admin.register(Employee)
class ViewEmployeeAdmin(ImportExportModelAdmin, EmployeeAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class EmployeePersonalInfoAdmin(admin.ModelAdmin):
    search_fields   = ['employee__first_name', 'employee__last_name']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = ['gender', 'blood_group', 'race', 'nationality']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'employee',
        'living_arrangement',
        'race',
        'nationality',
        'religion',
        'blood_group',
        'height',
        'weight',
        'military_status',
        'marital_status',
        'gender',
        'birth_date',
        'email',
        'phone',
        'created_at',
        'updated_at',
    ]

@admin.register(EmployeePersonalInfo)
class ViewEmployeePersonalInfoAdmin(ImportExportModelAdmin, EmployeePersonalInfoAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class EmployeeAddressAdmin(admin.ModelAdmin):
    search_fields   = ['employee__first_name', 'employee__last_name']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = ['province']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'employee',
        'address_type',
        'address_line_1',
        'address_line_2',
        'sub_district',
        'district',
        'province',
        'postal_code',
        'country',
        'phone',
        'created_at',
        'updated_at',
    ]

@admin.register(EmployeeAddress)
class ViewEmployeeAddressAdmin(ImportExportModelAdmin, EmployeeAddressAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
