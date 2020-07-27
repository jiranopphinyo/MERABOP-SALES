from django import forms
from django.forms import DateInput
from django.utils import timezone

### WAREHOUSE:: ALL
from WAREHOUSE.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DateInput(forms.DateInput):
    input_type = 'date'
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class ProductLotNumberModelForm(forms.ModelForm):
    class Meta:
        model   = ProductLotNumber
        fields  = "__all__"
        widgets = {
            'product'               : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'original_lot_number'   : forms.TextInput(attrs={'class': 'form-control'}),
            'received_date'         : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'receiving_amount'      : forms.NumberInput(attrs={'class': 'form-control'}),
            'remaining_amount'      : forms.NumberInput(attrs={'class': 'form-control'}),
            'manufactured_date'     : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'expired_date'          : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'unit_cost'             : forms.NumberInput(attrs={'class': 'form-control'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
