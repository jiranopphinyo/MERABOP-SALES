from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

### SALES:: ALL
from SALES.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'name', 'description', 'email', 'phone']
    list_display    = ['id', 'name', 'email', 'phone', 'created_at']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'name',
        'description',
        'email',
        'phone',
        'created_at',
        'updated_at',
    ]

@admin.register(Customer)
class ViewCustomerAdmin(ImportExportModelAdmin, CustomerAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerAddressAdmin(admin.ModelAdmin):
    search_fields   = ['customer__id', 'customer__name']
    list_display    = ['customer', 'address_name', 'address_line_1', 'sub_district', 'district', 'province', 'postal_code']
    list_editable   = []
    list_filter     = ['address_name']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'customer',
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

@admin.register(CustomerAddress)
class ViewCustomerAddressAdmin(ImportExportModelAdmin, CustomerAddressAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerContactPersonAdmin(admin.ModelAdmin):
    search_fields   = ['customer__id', 'customer__name', 'fullname', 'job_title', 'phone', 'email']
    list_display    = ['__str__', 'phone', 'email', 'is_active']
    list_editable   = ['is_active']
    list_filter     = ['is_active']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'customer',
        'fullname',
        'job_title',
        'phone',
        'email',
        'is_active',
        'created_at',
        'updated_at'
    ]

@admin.register(CustomerContactPerson)
class ViewCustomerContactPersonAdmin(ImportExportModelAdmin, CustomerContactPersonAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerPaymentTermAdmin(admin.ModelAdmin):
    search_fields   = ['customer__id', 'customer__name', 'payment_term__payment_term']
    list_display    = ['customer', 'payment_term', 'credit_day', 'credit_amount']
    list_editable   = []
    list_filter     = ['payment_term']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'customer',
        'payment_term',
        'credit_day',
        'credit_amount',
        'created_at',
        'updated_at',
    ]

@admin.register(CustomerPaymentTerm)
class ViewCustomerPaymentTermAdmin(ImportExportModelAdmin, CustomerPaymentTermAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PersonInChargeAdmin(admin.ModelAdmin):
    search_fields   = ['customer__id', 'customer__name', 'sales_reps__first_name', 'sales_reps__last_name']
    list_display    = ['customer', 'sales_reps']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'customer',
        'sales_reps',
        'created_at',
        'updated_at',
    ]

@admin.register(PersonInCharge)
class ViewPersonInChargeAdmin(ImportExportModelAdmin, PersonInChargeAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'date', 'estimate_needed_date', 'remark']
    list_display    = ['id', 'date', 'estimate_needed_date', 'remark']
    list_editable   = []
    list_filter     = ['estimate_needed_date']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'date',
        'estimate_needed_date',
        'remark',
        'created_at',
        'updated_at'
    ]

@admin.register(PurchaseRequisition)
class ViewPurchaseRequisitionAdmin(ImportExportModelAdmin, PurchaseRequisitionAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionItemAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'purchase_requisition__id', 'product__id', 'product__name']
    list_display    = ['__str__', 'quantity', 'unit_price']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'purchase_requisition',
        'product',
        'quantity',
        'unit_price',
        'remark',
        'created_at',
        'updated_at'
    ]

@admin.register(PurchaseRequisitionItem)
class ViewPurchaseRequisitionItemAdmin(ImportExportModelAdmin, PurchaseRequisitionItemAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionStatusLogAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'purchase_requisition__id', 'status__purchase_requisition_status', 'user']
    list_display    = ['__str__', 'user', 'remark']
    list_editable   = []
    list_filter     = ['status', 'user']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'purchase_requisition',
        'status',
        'user',
        'remark',
        'created_at',
        'updated_at'
    ]

@admin.register(PurchaseRequisitionStatusLog)
class ViewPurchaseRequisitionStatusLogAdmin(ImportExportModelAdmin, PurchaseRequisitionStatusLogAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'sales_reps__first_name', 'customer__id', 'customer__name']
    list_display    = ['id', 'customer', 'sales_reps', 'date', 'net_total']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'sub_total', 'after_discount', 'vat', 'net_total', 'baht_text', 'created_at', 'updated_at']
    fields          = [
        'id',
        'date',
        'valid_until',
        'estimate_delivery_day',
        'sales_reps',
        'customer',
        'customer_billing_address',
        'customer_contact_person',
        'payment_term',
        'sub_total',
        'discount',
        'after_discount',
        'vat',
        'net_total',
        'baht_text',
        'remark',
        'created_at',
        'updated_at',
    ]

@admin.register(Quotation)
class ViewQuotationAdmin(ImportExportModelAdmin, QuotationAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationItemAdmin(admin.ModelAdmin):
    search_fields   = ['quotation__id', 'quotation__sales_reps__first_name', 'quotation__customer__id', 'quotation__customer__name', 'product__id', 'product__name']
    list_display    = ['quotation', 'product', 'quantity', 'unit_price', 'amount']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'amount', 'created_at', 'updated_at']
    fields          = [
        'id',
        'quotation',
        'product',
        'quantity',
        'unit_price',
        'amount',
        'created_at',
        'updated_at',
    ]

@admin.register(QuotationItem)
class ViewQuotationItemAdmin(ImportExportModelAdmin, QuotationItemAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationStatusLogAdmin(admin.ModelAdmin):
    search_fields   = ['quotation__id', 'quotation__sales_reps__first_name', 'quotation__customer__id', 'quotation__customer__name', 'status__quotation_stauts', 'user']
    list_display    = ['quotation', 'status', 'user', 'remark']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'quotation',
        'status',
        'user',
        'remark',
        'created_at',
        'updated_at',
    ]

@admin.register(QuotationStatusLog)
class ViewQuotationStatusLogAdmin(ImportExportModelAdmin, QuotationStatusLogAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'sales_reps__first_name', 'customer__id', 'customer__name']
    list_display    = ['id', 'customer', 'sales_reps', 'date', 'net_total']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'sub_total', 'vat', 'net_total', 'baht_text', 'created_at', 'updated_at']
    fields          = [
        'id',
        'date',
        'delivery_date',
        'sales_reps',
        'customer',
        'customer_billing_address',
        'customer_delivery_address',
        'customer_payment_term',
        'sub_total',
        'vat',
        'net_total',
        'baht_text',
        'remark',
        'created_at',
        'updated_at',
    ]

@admin.register(SalesOrder)
class ViewSalesOrderAdmin(ImportExportModelAdmin, SalesOrderAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderItemAdmin(admin.ModelAdmin):
    search_fields   = ['sales_order__id', 'sales_order__sales_reps__first_name', 'sales_order__customer__id', 'sales_order__customer__name', 'product__id', 'product__name']
    list_display    = ['sales_order', 'product', 'quantity', 'unit_price', 'amount']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'amount', 'created_at', 'updated_at']
    fields          = [
        'id',
        'sales_order',
        'product',
        'quantity',
        'unit_price',
        'amount',
        'created_at',
        'updated_at',
    ]

@admin.register(SalesOrderItem)
class ViewSalesOrderItemAdmin(ImportExportModelAdmin, SalesOrderItemAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderStatusLogAdmin(admin.ModelAdmin):
    search_fields   = ['sales_order__id', 'sales_order__sales_reps__first_name', 'sales_order__customer__id', 'sales_order__customer__name', 'status__sales_order_stauts', 'user']
    list_display    = ['sales_order', 'status', 'user', 'remark']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'sales_order',
        'status',
        'user',
        'remark',
        'created_at',
        'updated_at',
    ]

@admin.register(SalesOrderStatusLog)
class ViewSalesOrderStatusLogAdmin(ImportExportModelAdmin, SalesOrderStatusLogAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportAdmin(admin.ModelAdmin):
    search_fields   = ['sales_reps__first_name', 'contact_method__daily_report_contact_method', 'customer__customer__id', 'customer__customer__name', 'customer_contact_person__fullname']
    list_display    = ['id', 'date', 'sales_reps', 'contact_method', 'customer', 'customer_contact_person']
    list_editable   = []
    list_filter     = ['sales_reps', 'contact_method', 'customer_contact_person']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'date',
        'sales_reps',
        'contact_method',
        'customer',
        'customer_contact_person',
        'created_at',
        'updated_at',
    ]

@admin.register(DailyReport)
class ViewDailyReportAdmin(ImportExportModelAdmin, DailyReportAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportItemAdmin(admin.ModelAdmin):
    search_fields   = ['daily_report__sales_reps__first_name', 'daily_report__contact_method__daily_report_contact_method', 'daily_report__customer__customer__id', 'daily_report__customer_contact_person__fullname']
    list_display    = ['__str__', 'product', 'daily_report_type', 'quantity', 'unit_price', 'is_accept']
    list_editable   = []
    list_filter     = ['daily_report_type']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'daily_report',
        'product',
        'daily_report_type',
        'quantity',
        'unit_price',
        'is_accept',
        'remark',
        'created_at',
        'updated_at',
    ]

@admin.register(DailyReportItem)
class ViewDailyReportItemAdmin(ImportExportModelAdmin, DailyReportItemAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
