from django.urls import path
from PURCHASE.views_supplier import *
from PURCHASE.views_product import *
from PURCHASE.views_purchase_order import *

app_name = "PURCHASE"
urlpatterns = [
    # SUPPLIER GENERAL INFO
    path('supplier/list/', supplier_list, name="supplier_list"),
    path('supplier/detail/<str:id>/', supplier_detail, name="supplier_detail"),
    path('supplier/create/', supplier_create, name="supplier_create"),
    path('supplier/update/<str:id>/', supplier_update, name="supplier_update"),
    # SUPPLIER ADDRESS INFO
    path('supplier/address/create/<str:id>/', supplier_address_create, name="supplier_address_create"),
    path('supplier/address/update/<str:id>/', supplier_address_update, name="supplier_address_update"),
    # SUPPLIER CONTACT PERSON INFO
    path('supplier/contact-person/create/<str:id>/', supplier_contact_person_create, name="supplier_contact_person_create"),
    path('supplier/contact-person/update/<str:id>/', supplier_contact_person_update, name="supplier_contact_person_update"),
    # SUPPLIER PAYMENT TERM INFO
    path('supplier/payment-term/create/<str:id>/', supplier_payment_term_create, name="supplier_payment_term_create"),
    path('supplier/payment-term/update/<str:id>/', supplier_payment_term_update, name="supplier_payment_term_update"),
    #======================================================================================================================================================================================#
    #======================================================================================================================================================================================#
    # PRODUCT GENERAL INFO
    path('product/list/', product_list, name="product_list"),
    path('product/detail/<str:id>/', product_detail, name="product_detail"),
    path('product/create/', product_create, name="product_create"),
    path('product/update/<str:id>/', product_update, name="product_update"),
    #======================================================================================================================================================================================#
    #======================================================================================================================================================================================#
    # PURCHASE ORDER
    path('purchase-order/list/', purchase_order_list, name="purchase_order_list"),
    path('purchase-order/detail/<str:id>/', purchase_order_detail, name="purchase_order_detail"),
    path('purchase-order/print/<str:id>/', purchase_order_print, name="purchase_order_print"),
    path('purchase-order/create/', purchase_order_create, name="purchase_order_create"),
    path('purchase-order/update/before-create/<str:id>/', purchase_order_update_before_create, name="purchase_order_update_before_create"),
    path('purchase-order/update/after-create/<str:id>/', purchase_order_update_after_create, name="purchase_order_update_after_create"),
    # PURCHASE ORDER ITEM INFO
    path('purchase-order/item/create/<str:id>/', purchase_order_item_create, name="purchase_order_item_create"),
    path('purchase-order/item/create/after-create/<str:id>/', purchase_order_item_create_after_create, name="purchase_order_item_create_after_create"),
    path('purchase-order/item/update/<str:id>/', purchase_order_item_update, name="purchase_order_item_update"),
    path('purchase-order/item/delete/<str:id>/', purchase_order_item_delete, name="purchase_order_item_delete"),
]