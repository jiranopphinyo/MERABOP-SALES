from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from SETTINGS.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CompanyAdmin(admin.ModelAdmin):
    search_fields   = ['company_name', 'brand_name']
    list_display    = ['__str__', 'address_line_1', 'sub_district', 'district', 'province', 'postal_code', 'email']
    readonly_fields = ['pk']
    fields          = [
        'pk',
        'company_name',
        'brand_name',
        'address_line_1',
        'address_line_2',
        'sub_district',
        'district',
        'province',
        'postal_code',
        'country',
        'phone',
        'fax',
        'email'
    ]

@admin.register(Company)
class ViewCompanyAdmin(ImportExportModelAdmin, CompanyAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierTypeAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'supplier_type']
    list_display    = ['supplier_type']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'supplier_type'
    ]

@admin.register(SupplierType)
class ViewSupplierTypeAdmin(ImportExportModelAdmin, SupplierTypeAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CountryAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'name']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'name'
    ]

@admin.register(Country)
class ViewCountryAdmin(ImportExportModelAdmin, CountryAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PaymentTermAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'payment_term']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'payment_term'
    ]

@admin.register(PaymentTerm)
class ViewPaymentTermAdmin(ImportExportModelAdmin, PaymentTermAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PackingTypeAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'packing_type']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'packing_type'
    ]

@admin.register(PackingType)
class ViewPackingTypeAdmin(ImportExportModelAdmin, PackingTypeAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PackingMaterialAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'packing_material']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'packing_material'
    ]

@admin.register(PackingMaterial)
class ViewPackingMaterialAdmin(ImportExportModelAdmin, PackingMaterialAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionStatusAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'purchase_requisition_status']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'purchase_requisition_status'
    ]

@admin.register(PurchaseRequisitionStatus)
class ViewPurchaseRequisitionStatusAdmin(ImportExportModelAdmin, PurchaseRequisitionStatusAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationStatusAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'quotation_status']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'quotation_status'
    ]

@admin.register(QuotationStatus)
class ViewQuotationStatusAdmin(ImportExportModelAdmin, QuotationStatusAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderStatusAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'sales_order_status']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'sales_order_status'
    ]

@admin.register(SalesOrderStatus)
class ViewSalesOrderStatusAdmin(ImportExportModelAdmin, SalesOrderStatusAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderStatusAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'purchase_order_status']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'purchase_order_status'
    ]

@admin.register(PurchaseOrderStatus)
class ViewPurchaseOrderStatusAdmin(ImportExportModelAdmin, PurchaseOrderStatusAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportContactMethodAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'daily_report_contact_method']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'daily_report_contact_method'
    ]

@admin.register(DailyReportContactMethod)
class ViewDailyReportContactMethodAdmin(ImportExportModelAdmin, DailyReportContactMethodAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportTypeAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'daily_report_type']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'daily_report_type'
    ]

@admin.register(DailyReportType)
class ViewDailyReportTypeAdmin(ImportExportModelAdmin, DailyReportTypeAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class LivingArrangementAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'living_arrangement']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'living_arrangement',
    ]

@admin.register(LivingArrangement)
class ViewLivingArrangementAdmin(ImportExportModelAdmin, LivingArrangementAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class RaceAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'race']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'race',
    ]
@admin.register(Race)
class ViewRaceAdmin(ImportExportModelAdmin, RaceAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class NationalityAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'nationality']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'nationality',
    ]
@admin.register(Nationality)
class ViewNationalityAdmin(ImportExportModelAdmin, NationalityAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DivisionAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'division']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'division',
    ]
@admin.register(Division)
class ViewDivisionAdmin(ImportExportModelAdmin, DivisionAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DepartmentAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'division__division', 'department']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'division',
        'department',
    ]
@admin.register(Department)
class ViewDepartmentAdmin(ImportExportModelAdmin, DepartmentAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SectionAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'department__division__division', 'department__department', 'section']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'department',
        'section',
    ]
@admin.register(Section)
class ViewSectionAdmin(ImportExportModelAdmin, SectionAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PositionAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'position']
    list_display    = ['__str__']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id']
    inlines         = []
    fields          = [
        'id',
        'position',
    ]
@admin.register(Position)
class ViewPositionAdmin(ImportExportModelAdmin, PositionAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
