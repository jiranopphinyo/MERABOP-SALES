from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

### PURCHASE:: ALL
from PURCHASE.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'name', 'supplier_type__supplier_type', 'description', 'email', 'website']
    list_display    = ['__str__', 'supplier_type', 'email', 'website', 'created_at']
    list_editable   = []
    list_filter     = ['supplier_type']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'name',
        'supplier_type',
        'description',
        'email',
        'website',
        'created_at',
        'updated_at',
    ]

@admin.register(Supplier)
class ViewSupplierAdmin(ImportExportModelAdmin, SupplierAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierAddressAdmin(admin.ModelAdmin):
    search_fields   = ['supplier__id', 'supplier__name']
    list_display    = ['supplier', 'address_name', 'address_line_1', 'sub_district', 'district', 'province', 'postal_code']
    list_editable   = []
    list_filter     = ['address_name']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'supplier',
        'address_name',
        'address_line_1',
        'address_line_2',
        'sub_district',
        'district',
        'province',
        'postal_code',
        'country',
        'phone',
        'fax',
        'created_at',
        'updated_at'
    ]

@admin.register(SupplierAddress)
class ViewSupplierAddressAdmin(ImportExportModelAdmin, SupplierAddressAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierContactPersonAdmin(admin.ModelAdmin):
    search_fields   = ['supplier__id', 'supplier__name', 'fullname', 'job_title', 'phone', 'email']
    list_display    = ['__str__', 'phone', 'email', 'is_active']
    list_editable   = ['is_active']
    list_filter     = ['is_active']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'supplier',
        'fullname',
        'job_title',
        'phone',
        'email',
        'is_active',
        'created_at',
        'updated_at'
    ]

@admin.register(SupplierContactPerson)
class ViewSupplierContactPersonAdmin(ImportExportModelAdmin, SupplierContactPersonAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierPaymentTermAdmin(admin.ModelAdmin):
    search_fields   = ['supplier__id', 'supplier__name', 'payment_term__payment_term']
    list_display    = ['supplier', 'payment_term', 'credit_day', 'credit_amount']
    list_editable   = []
    list_filter     = ['payment_term']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'supplier',
        'payment_term',
        'credit_day',
        'credit_amount',
        'created_at',
        'updated_at',
    ]

@admin.register(SupplierPaymentTerm)
class ViewSupplierPaymentTermAdmin(ImportExportModelAdmin, SupplierPaymentTermAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class ProductAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'name', 'characteristic', 'shipped_country__name', 'manufactured_country__name', 'supplier__id', 'supplier__name']
    list_display    = ['__str__', 'shipped_country', 'manufactured_country', 'total_remaining_amount', 'suggested_sales_price']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'total_remaining_amount', 'created_at', 'updated_at']
    fields          = [
        'id',
        'name',
        'net_weight',
        'gross_weight',
        'weighing_unit',
        'packing_type',
        'packing_material',
        'cbm',
        'characteristic',
        'shipped_country',
        'manufactured_country',
        'supplier',
        'total_remaining_amount',
        'suggeted_sales_price',
        'created_at',
        'updated_at',
    ]

@admin.register(Product)
class ViewProductAdmin(ImportExportModelAdmin, ProductAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'supplier__id', 'supplier__name']
    list_display    = ['id', 'date', 'supplier', 'sub_total', 'net_total']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'sub_total', 'vat', 'net_total', 'baht_text', 'created_at', 'updated_at']
    fields          = [
        'id',
        'date',
        'supplier',
        'supplier_billing_address',
        'supplier_contact_person',
        'supplier_payment_term',
        'sub_total',
        'vat',
        'net_total',
        'baht_text',
        'remark',
        'created_at',
        'updated_at',
    ]

@admin.register(PurchaseOrder)
class ViewPurchaseOrderAdmin(ImportExportModelAdmin, PurchaseOrderAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    search_fields   = ['purchase_order__id', 'purchase_order__customer__id', 'purchase_order__customer__name', 'product__id', 'product__name']
    list_display    = ['purchase_order', 'product', 'quantity', 'unit_price', 'amount']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'amount', 'created_at', 'updated_at']
    fields          = [
        'id',
        'purchase_order',
        'product',
        'quantity',
        'unit_price',
        'amount',
        'created_at',
        'updated_at'
    ]

@admin.register(PurchaseOrderItem)
class ViewPurchaseOrderItemAdmin(ImportExportModelAdmin, PurchaseOrderItemAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderStatusLogAdmin(admin.ModelAdmin):
    search_fields   = ['purchase_order__id', 'purchase_order__customer__id', 'purchase_order__customer__name', 'product__id', 'product__name', 'user', 'status__purchase_order_status']
    list_display    = ['purchase_order', 'status', 'user', 'remark']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'purchase_order',
        'status',
        'user',
        'remark',
        'created_at',
        'updated_at',
    ]

@admin.register(PurchaseOrderStatusLog)
class ViewPurchaseOrderStatusLogAdmin(ImportExportModelAdmin, PurchaseOrderStatusLogAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
