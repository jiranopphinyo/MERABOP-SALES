from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required


### SETTINGS:: ALL
from SETTINGS.decorators import *
### SALES:: ALL
from SALES.models import *
from SALES.forms import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def customer_list(request):
    customers   = Customer.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            customers   = Customer.objects.filter(
                Q(id__iexact                                = search_text) |
                Q(name__icontains                           = search_text) |
                Q(email__icontains                          = search_text) |
                Q(phone__icontains                          = search_text)
            )
        else:
            customers   = None
    
    return render(request, 'SALES/customer/customer_list.html', {
        'company'   : Company.objects.first(),
        'customers' : customers,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_detail(request, id):
    try:
        customer        = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer ID : {} does not exist.'.format(id)})

    addresses          = CustomerAddress.objects.filter(customer=id)
    contact_persons    = CustomerContactPerson.objects.filter(customer=id)
    payment_terms      = CustomerPaymentTerm.objects.filter(customer=id)

    return render(request, 'SALES/customer/customer_detail.html', {
        'company'               : Company.objects.first(),
        'customer'              : customer,
        'addresses'             : addresses,
        'contact_persons'       : contact_persons,
        'payment_terms'         : payment_terms,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_create(request):
    form        = CustomerModelForm()
    if request.method == 'POST':
        form    = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_customer_id    = Customer.objects.order_by('id').last().id
            return redirect('SALES:customer_detail', id=last_customer_id)

    return render(request, 'SALES/customer/general/customer_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_update(request, id):
    try:
        customer    = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer ID : {} does not exist.'.format(id)})
    
    form            = CustomerModelForm(instance=customer)
    if request.method == 'POST':
        form        = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('SALES:customer_detail', id=id)

    return render(request, 'SALES/customer/general/customer_update.html', {
        'company'               : Company.objects.first(),
        'customer'              : customer,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_address_create(request, id):
    try:
        customer    = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer ID : {} does not exist.'.format(id)})

    form        = CustomerAddressModelForm(initial={'customer': customer})
    if request.method == 'POST':
        form    = CustomerAddressModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:customer_detail', id=form.cleaned_data['customer'].id)

    return render(request, 'SALES/customer/address/customer_address_create.html', {
        'company'               : Company.objects.first(),
        'customer'              : customer,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_address_update(request, id):
    try:
        customer_address    = CustomerAddress.objects.get(id=id)
    except CustomerAddress.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer Address ID : {} does not exist.'.format(id)})
    
    form            = CustomerAddressModelForm(instance=customer_address)
    if request.method == 'POST':
        form        = CustomerAddressModelForm(request.POST, instance=customer_address)
        if form.is_valid():
            form.save()
            return redirect('SALES:customer_detail', id=form.cleaned_data['customer'].id)

    return render(request, 'SALES/customer/address/customer_address_update.html', {
        'company'               : Company.objects.first(),
        'customer_address'      : customer_address,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_contact_person_create(request, id):
    try:
        customer    = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer ID : {} does not exist.'.format(id)})

    form        = CustomerContactPersonModelForm(initial={'customer': customer})
    if request.method == 'POST':
        form    = CustomerContactPersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:customer_detail', id=form.cleaned_data['customer'].id)

    return render(request, 'SALES/customer/contact_person/customer_contact_person_create.html', {
        'company'               : Company.objects.first(),
        'customer'              : customer,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_contact_person_update(request, id):
    try:
        customer_contact_person = CustomerContactPerson.objects.get(id=id)
    except CustomerContactPerson.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer Contact Person ID : {} does not exist.'.format(id)})
    
    form            = CustomerContactPersonModelForm(instance=customer_contact_person)
    if request.method == 'POST':
        form        = CustomerContactPersonModelForm(request.POST, instance=customer_contact_person)
        if form.is_valid():
            form.save()
            return redirect('SALES:customer_detail', id=form.cleaned_data['customer'].id)

    return render(request, 'SALES/customer/contact_person/customer_contact_person_update.html', {
        'company'               : Company.objects.first(),
        'customer_contact_person'      : customer_contact_person,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_payment_term_create(request, id):
    try:
        customer    = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer ID : {} does not exist.'.format(id)})

    form        = CustomerPaymentTermModelForm(initial={'customer': customer})
    if request.method == 'POST':
        form    = CustomerPaymentTermModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:customer_detail', id=form.cleaned_data['customer'].id)

    return render(request, 'SALES/customer/payment_term/customer_payment_term_create.html', {
        'company'               : Company.objects.first(),
        'customer'              : customer,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def customer_payment_term_update(request, id):
    try:
        customer_payment_term = CustomerPaymentTerm.objects.get(id=id)
    except CustomerPaymentTerm.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Customer Payment Term ID : {} does not exist.'.format(id)})
    
    form            = CustomerPaymentTermModelForm(instance=customer_payment_term)
    if request.method == 'POST':
        form        = CustomerPaymentTermModelForm(request.POST, instance=customer_payment_term)
        if form.is_valid():
            form.save()
            return redirect('SALES:customer_detail', id=form.cleaned_data['customer'].id)

    return render(request, 'SALES/customer/payment_term/customer_payment_term_update.html', {
        'company'               : Company.objects.first(),
        'customer_payment_term' : customer_payment_term,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
