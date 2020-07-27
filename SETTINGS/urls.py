from django.urls import path
from SETTINGS.views import *
from SETTINGS.views_settings import *

app_name = "SETTINGS"

urlpatterns = [
    path('', main_dashboard, name="main_dashboard"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    path('unauthorized/', unauthorized, name="unauthorized"),
    path('unassigned-roles/', unassigned_roles, name="unassigned_roles"),
    #========================================================================================================================================================================================================================================================#
    #========================================================================================================================================================================================================================================================#
    path('ajax/load_customer_billing_address/', load_customer_billing_address, name="ajax_load_customer_billing_address"),
    path('ajax/load_customer_contact_person/', load_customer_contact_person, name="ajax_load_customer_contact_person"),
    path('ajax/load_customer_payment_term/', load_customer_payment_term, name="ajax_load_customer_payment_term"),
    path('ajax/load_sales_reps/', load_sales_reps, name="ajax_load_sales_reps"),
    #========================================================================================================================================================================================================================================================#
    #========================================================================================================================================================================================================================================================#
    # SETTINGS
    path('settings/', settings, name="settings"),
    # SETTINGS:: COMPANY
    path('settings/company/create/', settings_company_create, name="settings_company_create"),
    path('settings/company/update/<str:id>/', settings_company_update, name="settings_company_update"),
    # SETTINGS:: SUPPLIER TYPE
    path('settings/supplier-type/create/', settings_supplier_type_create, name="settings_supplier_type_create"),
    path('settings/supplier-type/update/<str:id>/', settings_supplier_type_update, name="settings_supplier_type_update"),
    # SETTINGS:: PACKING TYPE
    path('settings/packing-type/create/', settings_packing_type_create, name="settings_packing_type_create"),
    path('settings/packing-type/update/<str:id>/', settings_packing_type_update, name="settings_packing_type_update"),
    # SETTINGS:: PACKING MATERIAL
    path('settings/packing-material/create/', settings_packing_material_create, name="settings_packing_material_create"),
    path('settings/packing-material/update/<str:id>/', settings_packing_material_update, name="settings_packing_material_update"),
    # SETTINGS:: PURCHASE ORDER STATUS
    path('settings/purchase-order/status/create/', settings_purchase_order_status_create, name="settings_purchase_order_status_create"),
    path('settings/purchase-order/status/update/<str:id>/', settings_purchase_order_status_update, name="settings_purchase_order_status_update"),
    # SETTINGS:: PURCHASE REQUISITION STATUS
    path('settings/purchase-requisition/status/create/', settings_purchase_requisition_status_create, name="settings_purchase_requisition_status_create"),
    path('settings/purchase-requisition/status/update/<str:id>/', settings_purchase_requisition_status_update, name="settings_purchase_requisition_status_update"),
    # SETTINGS:: QUOTATION STATUS
    path('settings/quotation/status/create/', settings_quotation_status_create, name="settings_quotation_status_create"),
    path('settings/quotation/status/update/<str:id>/', settings_quotation_status_update, name="settings_quotation_status_update"),
    # SETTINGS:: SALES ORDER STATUS
    path('settings/sales-order/status/create/', settings_sales_order_status_create, name="settings_sales_order_status_create"),
    path('settings/sales-order/status/update/<str:id>/', settings_sales_order_status_update, name="settings_sales_order_status_update"),
    # SETTINGS:: DAILY REPORT CONTACT METHOD
    path('settings/daily-report/contact-method/create/', settings_daily_report_contact_method_create, name="settings_daily_report_contact_method_create"),
    path('settings/daily-report/contact-method/update/<str:id>/', settings_daily_report_contact_method_update, name="settings_daily_report_contact_method_update"),
    # SETTINGS:: DAILY REPORT TYPE
    path('settings/daily-report-type/create/', settings_daily_report_type_create, name="settings_daily_report_type_create"),
    path('settings/daily-report-type/update/<str:id>/', settings_daily_report_type_update, name="settings_daily_report_type_update"),
    # SETTINGS:: LIVING ARRANGEMENT
    path('settings/living-arrangement/create/', settings_living_arrangement_create, name="settings_living_arrangement_create"),
    path('settings/living-arrangement/update/<str:id>/', settings_living_arrangement_update, name="settings_living_arrangement_update"),
    # SETTINGS:: RACE
    path('settings/race/create/', settings_race_create, name="settings_race_create"),
    path('settings/race/update/<str:id>/', settings_race_update, name="settings_race_update"),
    # SETTINGS:: NATIONALITY
    path('settings/nationality/create/', settings_nationality_create, name="settings_nationality_create"),
    path('settings/nationality/update/<str:id>/', settings_nationality_update, name="settings_nationality_update"),
    # SETTINGS:: DIVISION
    path('settings/division/create/', settings_division_create, name="settings_division_create"),
    path('settings/division/update/<str:id>/', settings_division_update, name="settings_division_update"),
    # SETTINGS:: DEPARTMENT
    path('settings/department/create/', settings_department_create, name="settings_department_create"),
    path('settings/department/update/<str:id>/', settings_department_update, name="settings_department_update"),
    # SETTINGS:: SECTION
    path('settings/section/create/', settings_section_create, name="settings_section_create"),
    path('settings/section/update/<str:id>/', settings_section_update, name="settings_section_update"),
    # SETTINGS:: POSITION
    path('settings/position/create/', settings_position_create, name="settings_position_create"),
    path('settings/position/update/<str:id>/', settings_position_update, name="settings_position_update"),
]