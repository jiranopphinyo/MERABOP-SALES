from django.urls import path
from SALES.views_customer import *
from SALES.views_person_in_charge import *
from SALES.views_purchase_requisition import *
from SALES.views_quotation import *
from SALES.views_sales_order import *
from SALES.views_daily_report import *

app_name = "SALES"
urlpatterns = [
    # CUSTOMER GENERAL INFO
    path('customer/list/', customer_list, name="customer_list"),
    path('customer/detail/<str:id>/', customer_detail, name="customer_detail"),
    path('customer/create/', customer_create, name="customer_create"),
    path('customer/update/<str:id>/', customer_update, name="customer_update"),
    # CUSTOMER ADDRESS INFO
    path('customer/address/create/<str:id>/', customer_address_create, name="customer_address_create"),
    path('customer/address/update/<str:id>/', customer_address_update, name="customer_address_update"),
    # CUSTOMER CONTACT PERSON INFO
    path('customer/contact-person/create/<str:id>/', customer_contact_person_create, name="customer_contact_person_create"),
    path('customer/contact-person/update/<str:id>/', customer_contact_person_update, name="customer_contact_person_update"),
    # CUSTOMER PAYMENT TERM INFO
    path('customer/payment-term/create/<str:id>/', customer_payment_term_create, name="customer_payment_term_create"),
    path('customer/payment-term/update/<str:id>/', customer_payment_term_update, name="customer_payment_term_update"),
    #======================================================================================================================================================================================#
    #======================================================================================================================================================================================#
    # PERSON IN CHARGE INFO
    path('person-in-charge/list/', person_in_charge_list, name="person_in_charge_list"),
    path('person-in-charge/create/', person_in_charge_create, name="person_in_charge_create"),
    #======================================================================================================================================================================================#
    #======================================================================================================================================================================================#
    # PURCHASE REQUISITION GENERAL INFO
    path('purchase-requisition/list/', purchase_requisition_list, name="purchase_requisition_list"),
    path('purchase-requisition/detail/<str:id>/', purchase_requisition_detail, name="purchase_requisition_detail"),
    path('purchase-requisition/create/', purchase_requisition_create, name="purchase_requisition_create"),
    path('purchase-requisition/update/before-create/<str:id>/', purchase_requisition_update_before_create, name="purchase_requisition_update_before_create"),
    path('purchase-requisition/update/after-create/<str:id>/', purchase_requisition_update_after_create, name="purchase_requisition_update_after_create"),
    path('purchase-requisition/print/<str:id>/', purchase_requisition_print, name="purchase_requisition_print"),
    # PURCHASE REQUISITION ITEM INFO
    path('purchase-requisition/item/create/<str:id>/', purchase_requisition_item_create, name="purchase_requisition_item_create"),
    path('purchase-requisition/item/create/after-create/<str:id>/', purchase_requisition_item_create_after_create, name="purchase_requisition_item_create_after_create"),
    path('purchase-requisition/item/update/<str:id>/', purchase_requisition_item_update, name="purchase_requisition_item_update"),
    path('purchase-requisition/item/delete/<str:id>/', purchase_requisition_item_delete, name="purchase_requisition_item_delete"),
    #======================================================================================================================================================================================#
    #======================================================================================================================================================================================#
    # QUOTATION GENERAL INFO
    path('quotation/list/', quotation_list, name="quotation_list"),
    path('quotation/detail/<str:id>/', quotation_detail, name="quotation_detail"),
    path('quotation/create/', quotation_create, name="quotation_create"),
    path('quotation/update/before-create/<str:id>/', quotation_update_before_create, name="quotation_update_before_create"),
    path('quotation/update/after-create/<str:id>/', quotation_update_after_create, name="quotation_update_after_create"),
    path('quotation/print/<str:id>/', quotation_print, name="quotation_print"),
    # QUOTATION ITEM INFO
    path('quotation/item/create/<str:id>/', quotation_item_create, name="quotation_item_create"),
    path('quotation/item/create/after-create/<str:id>/', quotation_item_create_after_create, name="quotation_item_create_after_create"),
    path('quotation/item/update/<str:id>/', quotation_item_update, name="quotation_item_update"),
    path('quotation/item/delete/<str:id>/', quotation_item_delete, name="quotation_item_delete"),
    #======================================================================================================================================================================================#
    #======================================================================================================================================================================================#
    # SALES ORDER GENERAL INFO
    path('sales-order/list/', sales_order_list, name="sales_order_list"),
    path('sales-order/detail/<str:id>/', sales_order_detail, name="sales_order_detail"),
    path('sales-order/create/', sales_order_create, name="sales_order_create"),
    path('sales-order/update/before-create/<str:id>/', sales_order_update_before_create, name="sales_order_update_before_create"),
    path('sales-order/update/after-create/<str:id>/', sales_order_update_after_create, name="sales_order_update_after_create"),
    path('sales-order/print/<str:id>/', sales_order_print, name="sales_order_print"),
    # SALES ORDER ITEM INFO
    path('sales-order/item/create/<str:id>/', sales_order_item_create, name="sales_order_item_create"),
    path('sales-order/item/create/after-create/<str:id>/', sales_order_item_create_after_create, name="sales_order_item_create_after_create"),
    path('sales-order/item/update/<str:id>/', sales_order_item_update, name="sales_order_item_update"),
    path('sales-order/item/delete/<str:id>/', sales_order_item_delete, name="sales_order_item_delete"),
    #======================================================================================================================================================================================#
    #======================================================================================================================================================================================#
    # DAILY REPORT GENERAL INFO
    path('daily-report/list/', daily_report_list, name="daily_report_list"),
    path('daily-report/detail/<str:id>/', daily_report_detail, name="daily_report_detail"),
    path('daily-report/create/', daily_report_create, name="daily_report_create"),
    path('daily-report/update/before-create/<str:id>/', daily_report_update_before_create, name="daily_report_update_before_create"),
    path('daily-report/update/after-create/<str:id>/', daily_report_update_after_create, name="daily_report_update_after_create"),
    # DAILY REPORT ITEM INFO
    path('daily-report/item/create/<str:id>/', daily_report_item_create, name="daily_report_item_create"),
]