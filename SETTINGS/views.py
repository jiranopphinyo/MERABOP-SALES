from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
### DJANGO AUTHENTICATION
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
### SETTINGS:: ALL
from SETTINGS.models import *
from SETTINGS.decorators import *
### PURCHASE:: ALL
from PURCHASE.models import *
### SALES:: ALL
from SALES.models import *
### WAREHOUSE:: ALL
from WAREHOUSE.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
def main_dashboard(request):
    return render(request, 'MAIN/main_dashboard.html', {
        'company'           : Company.objects.first(),
        'total_customer'    : Customer.objects.count(),
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('SETTINGS:main_dashboard')
        else:
            message.info(request, 'Username or password is not correct.')

    return render(request, 'MAIN/login.html', {
        'company': Company.objects.first(),
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def logout_page(request):
    logout(request)
    return redirect('SETTINGS:login')
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def unauthorized(request):
    return render(request, 'MAIN/unauthorized.html', {
        'company': Company.objects.first(),
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def unassigned_roles(request):
    return render(request, 'MAIN/unassigned_roles.html', {
        'company': Company.objects.first(),
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def load_customer_billing_address(request):
    customer_id         = request.GET.get('address_1')
    billing_address     = CustomerAddress.objects.filter(customer=customer_id)
    return render(request, 'SETTINGS/dropdown/customer_billing_address.html', {'billing_address': billing_address})

def load_customer_contact_person(request):
    customer_id         = request.GET.get('address_2')
    contact_persons     = CustomerContactPerson.objects.filter(customer=customer_id).order_by('-created_at')
    return render(request, 'SETTINGS/dropdown/customer_contact_person.html', {'contact_persons': contact_persons})

def load_customer_payment_term(request):
    customer_id         = request.GET.get('address_3')
    payment_terms       = CustomerPaymentTerm.objects.filter(customer=customer_id).order_by('-created_at')
    return render(request, 'SETTINGS/dropdown/customer_payment_term.html', {'payment_terms': payment_terms})

def load_sales_reps(request):
    customer_id         = request.GET.get('customer_1')
    sales_reps          = PersonInCharge.objects.filter(customer=customer_id)
    return render(request, 'SETTINGS/dropdown/person_in_charge.html', {'sales_reps': sales_reps})
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
