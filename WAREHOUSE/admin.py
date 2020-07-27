from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

### WAREHOUSE:: ALL
from WAREHOUSE.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class ProductLotNumberAdmin(admin.ModelAdmin):
    search_fields   = ['id', 'product__id', 'product__name', 'original_lot_number']
    list_display    = ['id', 'product', 'received_date', 'receiving_amount', 'manufactured_date', 'expired_date']
    list_editable   = []
    list_filter     = []
    readonly_fields = ['id', 'created_at', 'updated_at']
    fields          = [
        'id',
        'product',
        'original_lot_number',
        'received_date',
        'receiving_amount',
        'remaining_amount',
        'manufactured_date',
        'expired_date',
        'unit_cost',
        'remark',
        'created_at',
        'updated_at'
    ]

@admin.register(ProductLotNumber)
class ViewProductLotNumberAdmin(ImportExportModelAdmin, ProductLotNumberAdmin):
    pass
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
