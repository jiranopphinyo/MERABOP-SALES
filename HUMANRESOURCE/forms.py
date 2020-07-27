from django import forms
from django.contrib.auth.models import User
from django.utils import timezone


### HUMANRESOURCE:: ALL
from HUMANRESOURCE.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DateInput(forms.DateInput):
    input_type = 'date'
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class UserModelForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = ['username', 'first_name', 'last_name', 'password', 'groups', 'is_staff', 'is_active']
        widgets = {
            'username'      : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name'    : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name'     : forms.TextInput(attrs={'class': 'form-control'}),
            'password'      : forms.PasswordInput(attrs={'class': 'form-control'}),
            'groups'        : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'is_staff'      : forms.CheckboxInput(attrs={'checked': 'true'}),
            'is_active'     : forms.CheckboxInput(attrs={'checked': 'true'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model   = Employee
        fields  = "__all__"
        widgets = {
            'user'          : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'first_name'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'},)
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class EmployeePersonalInfoModelForm(forms.ModelForm):
    class Meta:
        model   = EmployeePersonalInfo
        fields  = "__all__"
        widgets = {
            'employee'              : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'living_arrangement'    : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'race'                  : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'nationality'           : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'religion'              : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'blood_group'           : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'height'                : forms.NumberInput(attrs={'class': 'form-control'}),
            'weight'                : forms.NumberInput(attrs={'class': 'form-control'}),
            'military_status'       : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'marital_status'        : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'gender'                : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'birth_date'            : forms.DateInput(attrs={'class': 'form-control', 'data-provide': 'datepicker', 'data-date-format': 'yyyy-mm-dd', 'data-date-autoclose': 'true'}),
            'email'                 : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'phone'                 : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+66)_-___-____ / (+66)__-___-____'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class EmployeeAddressModelForm(forms.ModelForm):
    class Meta:
        model   = EmployeeAddress
        fields  = "__all__"
        widgets = {
            'employee'              : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'address_type'          : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
            'address_line_1'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House name/number and street, etc.'}),
            'address_line_2'        : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment, suite, unit, building, floor, etc.'}),
            'sub_district'          : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub District / Tumbol'}),
            'district'              : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District / Amphoe'}),
            'province'              : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Province'}),
            'postal_code'           : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP / Postal Code'}),
            'country'               : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'phone'                 : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(+66)_-___-____ / (+66)__-___-____'}),
        }
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
