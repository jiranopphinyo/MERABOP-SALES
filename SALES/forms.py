from django import forms
from django.forms import DateInput
from django.utils import timezone

### SALES:: ALL
from SALES.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DateInput(forms.DateInput):
    input_type = 'date'
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerModelForm(forms.ModelForm):
    class Meta:
        model   = Customer
        fields  = "__all__"
        widgets = {
            'name'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'description'   : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'email'         : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'phone'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+66)_-___-____ / (+66)__-___-____'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerAddressModelForm(forms.ModelForm):
    class Meta:
        model   = CustomerAddress
        fields  = "__all__"
        widgets = {
            'customer'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
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
class CustomerContactPersonModelForm(forms.ModelForm):
    class Meta:
        model   = CustomerContactPerson
        fields  = "__all__"
        widgets = {
            'customer'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'fullname'      : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. John Doe'}),
            'job_title'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Purchasing Manager'}),
            'phone'         : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+66)_-___-____ / (+66)__-___-____'}),
            'email'         : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. email@example.com'}),
            'is_active'     : forms.Select(choices=((True, "Yes"), (False, "No")), attrs={'class': 'select2 form-control', 'data-toggle': 'select2'})
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerPaymentTermModelForm(forms.ModelForm):
    class Meta:
        model   = CustomerPaymentTerm
        fields  = "__all__"
        widgets = {
            'customer'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'payment_term'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'credit_day'    : forms.NumberInput(attrs={'class': 'form-control'}),
            'credit_amount' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PersonInChargeModelForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(PersonInChargeModelForm, self).__init__(*args, **kwargs)
    #     self.fields['sales_reps'].queryset      = Employee.objects.filter(section__in=['', '', ''])
    
    class Meta:
        model   = PersonInCharge
        fields  = "__all__"
        widgets = {
            'customer'      : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'sales_reps'    : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionModelForm(forms.ModelForm):
    class Meta:
        model   = PurchaseRequisition
        fields  = "__all__"
        widgets = {
            'date'                  : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'estimate_needed_date'  : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionItemModelForm(forms.ModelForm):
    class Meta:
        model   = PurchaseRequisitionItem
        fields  = "__all__"
        widgets = {
            'purchase_requisition'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'product'               : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'quantity'              : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price'            : forms.NumberInput(attrs={'class': 'form-control'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionStatusLogModelForm(forms.ModelForm):
    class Meta:
        model   = PurchaseRequisitionStatusLog
        fields  = "__all__"
        widgets = {
            'purchase_requisition'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'status'                : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'user'                  : forms.TextInput(attrs={'class': 'form-control'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationModelForm(forms.ModelForm):
    class Meta:
        model   = Quotation
        exclude = ['sub_total', 'after_discount', 'vat', 'net_total', 'baht_text']
        widgets = {
            'date'                  : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'valid_until'           : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'estimate_delivery_day' : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'sales_reps'            : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer'              : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer_billing_address'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer_contact_person'   : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'payment_term'          : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'discount'              : forms.NumberInput(attrs={'class': 'form-control'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationItemModelForm(forms.ModelForm):
    class Meta:
        model   = QuotationItem
        fields  = "__all__"
        widgets = {
            'quotation'             : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'product'               : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'quantity'              : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price'            : forms.NumberInput(attrs={'class': 'form-control'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationStatusLogModelForm(forms.ModelForm):
    class Meta:
        model   = QuotationStatusLog
        fields  = "__all__"
        widgets = {
            'quotation'             : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'status'                : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'user'                  : forms.TextInput(attrs={'class': 'form-control'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderModelForm(forms.ModelForm):
    class Meta:
        model   = SalesOrder
        exclude = ['sub_total', 'vat', 'net_total', 'baht_text']
        widgets = {
            'date'                  : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'delivery_date'         : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'sales_reps'            : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer'              : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer_billing_address'  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer_delivery_address' : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer_payment_term' : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderItemModelForm(forms.ModelForm):
    class Meta:
        model   = SalesOrderItem
        fields  = "__all__"
        widgets = {
            'sales_order'           : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'product'               : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'quantity'              : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price'            : forms.NumberInput(attrs={'class': 'form-control'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderStatusLogModelForm(forms.ModelForm):
    class Meta:
        model   = SalesOrderStatusLog
        fields  = "__all__"
        widgets = {
            'sales_order'           : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'status'                : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'user'                  : forms.TextInput(attrs={'class': 'form-control'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportModelForm(forms.ModelForm):
    class Meta:
        model   = DailyReport
        fields  = "__all__"
        widgets = {
            'date'                  : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'sales_reps'            : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'contact_method'        : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer'              : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'customer_contact_person': forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportItemModelForm(forms.ModelForm):
    class Meta:
        model   = DailyReportItem
        fields  = "__all__"
        widgets = {
            'daily_report'          : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'product'               : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'daily_report_type'     : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'quantity'              : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price'            : forms.NumberInput(attrs={'class': 'form-control'}),
            'is_accept'             : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'remark'                : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
