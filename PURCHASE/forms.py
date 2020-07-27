from django import forms
from django.utils import timezone

### PURCHASE:: ALL
from PURCHASE.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DateInput(forms.DateInput):
    input_type = 'date'
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierModelForm(forms.ModelForm):
    class Meta:
        model   = Supplier
        fields  = "__all__"
        widgets = {
            'name'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Name'}),
            'supplier_type' : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'description'   : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'email'         : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'website'       : forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.example.com'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierAddressModelForm(forms.ModelForm):
    class Meta:
        model   = SupplierAddress
        fields  = "__all__"
        widgets = {
            'supplier'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'address_name'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Head Office / Warehouse #1 / Factory #1'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address No., Building, Room, Floor'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alley, Road, Industrial Estate'}),
            'sub_district'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub - District / Tumbol'}),
            'district'      : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District / Amphoe'}),
            'province'      : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provice / State / City'}),
            'postal_code'   : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP Code / Postal Code'}),
            'country'       : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'phone'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+66)_-___-____ / (+66)__-___-____'}),
            'fax'           : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+66)_-___-____'})
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierContactPersonModelForm(forms.ModelForm):
    class Meta:
        model   = SupplierContactPerson
        fields  = "__all__"
        widgets = {
            'supplier'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'fullname'      : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. John Doe'}),
            'job_title'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Sales Manager'}),
            'phone'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+66)_-___-____ / (+66)__-___-____'}),
            'email'         : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. email@example.com'}),
            'is_active'     : forms.Select(choices=((True, "Yes"), (False, "No")), attrs={'class': 'select2 form-control', 'data-toggle': 'select2'})
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierPaymentTermModelForm(forms.ModelForm):
    class Meta:
        model   = SupplierPaymentTerm
        fields  = "__all__"
        widgets = {
            'supplier'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'payment_term'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'credit_day'    : forms.NumberInput(attrs={'class': 'form-control'}),
            'credit_amount' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class ProductModelForm(forms.ModelForm):
    class Meta:
        model   = Product
        fields  = "__all__"
        widgets = {
            'id'                    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product ID'}),
            'name'                  : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'net_weight'            : forms.NumberInput(attrs={'class': 'form-control'}),
            'gross_weight'          : forms.NumberInput(attrs={'class': 'form-control'}),
            'weighing_unit'         : forms.TextInput(attrs={'class': 'form-control'}),
            'packing_type'          : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'packing_material'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'cbm'                   : forms.NumberInput(attrs={'class': 'form-control'}),
            'characteristic'        : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'shipped_country'       : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'manufactured_country'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'supplier'              : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'suggested_sales_price' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderModelForm(forms.ModelForm):
    class Meta:
        model   = PurchaseOrder
        fields  = "__all__"
        widgets = {
            'date'                      : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'supplier'                  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'supplier_billing_address'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'supplier_contact_person'   : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'supplier_payment_term'     : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'remark'                    : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderItemModelForm(forms.ModelForm):
    class Meta:
        model   = PurchaseOrderItem
        fields  = "__all__"
        widgets = {
            'purchase_order'        : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'product'               : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'quantity'              : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price'            : forms.NumberInput(attrs={'class': 'form-control'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderStatusLogModelForm(forms.ModelForm):
    class Meta:
        model   = PurchaseOrderStatusLog
        fields  = "__all__"
        widgets = {
            'purchase_order'        : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'status'                : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'user'                  : forms.TextInput(attrs={'class': 'form-control'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
