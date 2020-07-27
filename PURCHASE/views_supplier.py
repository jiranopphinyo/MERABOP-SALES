from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required

### SETTINGS:: ALL
from SETTINGS.decorators import *
### PURCHASE:: ALL
from PURCHASE.models import *
from PURCHASE.forms import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def supplier_list(request):
    suppliers   = Supplier.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            suppliers   = Supplier.objects.filter(
                Q(id__iexact                                = search_text) |
                Q(name__icontains                           = search_text) |
                Q(email__icontains                          = search_text) |
                Q(website__icontains                        = search_text) |
                Q(supplier_type__supplier_type__icontains   = search_text)
            )
        else:
            suppliers   = None
    
    return render(request, 'PURCHASE/supplier/supplier_list.html', {
        'company'       : Company.objects.first(),
        'suppliers'     : suppliers,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_detail(request, id):
    try:
        supplier        = Supplier.objects.get(id=id)
    except Supplier.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier ID : {} does not exist.'.format(id)})

    addresses           = SupplierAddress.objects.filter(supplier=id)
    contact_persons     = SupplierContactPerson.objects.filter(supplier=id)
    payment_terms       = SupplierPaymentTerm.objects.filter(supplier=id)
    products            = Product.objects.filter(supplier=id)

    return render(request, 'PURCHASE/supplier/supplier_detail.html', {
        'company'           : Company.objects.first(),
        'supplier'          : supplier,
        'addresses'         : addresses,
        'contact_persons'   : contact_persons,
        'payment_terms'     : payment_terms,
        'products'          : products,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_create(request):
    form        = SupplierModelForm()
    if request.method == 'POST':
        form    = SupplierModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_supplier_id    = Supplier.objects.order_by('id').last().id
            return redirect('PURCHASE:supplier_detail', id=last_supplier_id)

    return render(request, 'PURCHASE/supplier/general/supplier_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_update(request, id):
    try:
        supplier    = Supplier.objects.get(id=id)
    except Supplier.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier ID : {} does not exist.'.format(id)})
    
    form            = SupplierModelForm(instance=supplier)
    if request.method == 'POST':
        form        = SupplierModelForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:supplier_detail', id=id)

    return render(request, 'PURCHASE/supplier/general/supplier_update.html', {
        'company'               : Company.objects.first(),
        'supplier'              : supplier,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_address_create(request, id):
    try:
        supplier    = Supplier.objects.get(id=id)
    except Supplier.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier ID : {} does not exist.'.format(id)})

    form        = SupplierAddressModelForm(initial={'supplier': supplier})
    if request.method == 'POST':
        form    = SupplierAddressModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:supplier_detail', id=form.cleaned_data['supplier'].id)

    return render(request, 'PURCHASE/supplier/address/supplier_address_create.html', {
        'company'               : Company.objects.first(),
        'supplier'              : supplier,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_address_update(request, id):
    try:
        supplier_address    = SupplierAddress.objects.get(id=id)
    except SupplierAddress.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier Address ID : {} does not exist.'.format(id)})
    
    form            = SupplierAddressModelForm(instance=supplier_address)
    if request.method == 'POST':
        form        = SupplierAddressModelForm(request.POST, instance=supplier_address)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:supplier_detail', id=form.cleaned_data['supplier'].id)

    return render(request, 'PURCHASE/supplier/address/supplier_address_update.html', {
        'company'               : Company.objects.first(),
        'supplier_address'      : supplier_address,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_contact_person_create(request, id):
    try:
        supplier    = Supplier.objects.get(id=id)
    except Supplier.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier ID : {} does not exist.'.format(id)})

    form        = SupplierContactPersonModelForm(initial={'supplier': supplier})
    if request.method == 'POST':
        form    = SupplierContactPersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:supplier_detail', id=form.cleaned_data['supplier'].id)

    return render(request, 'PURCHASE/supplier/contact_person/supplier_contact_person_create.html', {
        'company'               : Company.objects.first(),
        'supplier'              : supplier,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_contact_person_update(request, id):
    try:
        supplier_contact_person = SupplierContactPerson.objects.get(id=id)
    except SupplierContactPerson.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier Contact Person ID : {} does not exist.'.format(id)})
    
    form            = SupplierContactPersonModelForm(instance=supplier_contact_person)
    if request.method == 'POST':
        form        = SupplierContactPersonModelForm(request.POST, instance=supplier_contact_person)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:supplier_detail', id=form.cleaned_data['supplier'].id)

    return render(request, 'PURCHASE/supplier/contact_person/supplier_contact_person_update.html', {
        'company'               : Company.objects.first(),
        'supplier_contact_person'      : supplier_contact_person,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_payment_term_create(request, id):
    try:
        supplier    = Supplier.objects.get(id=id)
    except Supplier.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier ID : {} does not exist.'.format(id)})

    form        = SupplierPaymentTermModelForm(initial={'supplier': supplier})
    if request.method == 'POST':
        form    = SupplierPaymentTermModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:supplier_detail', id=form.cleaned_data['supplier'].id)

    return render(request, 'PURCHASE/supplier/payment_term/supplier_payment_term_create.html', {
        'company'               : Company.objects.first(),
        'supplier'              : supplier,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def supplier_payment_term_update(request, id):
    try:
        supplier_payment_term = SupplierPaymentTerm.objects.get(id=id)
    except SupplierPaymentTerm.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier Payment Term ID : {} does not exist.'.format(id)})
    
    form            = SupplierPaymentTermModelForm(instance=supplier_payment_term)
    if request.method == 'POST':
        form        = SupplierPaymentTermModelForm(request.POST, instance=supplier_payment_term)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:supplier_detail', id=form.cleaned_data['supplier'].id)

    return render(request, 'PURCHASE/supplier/payment_term/supplier_payment_term_update.html', {
        'company'               : Company.objects.first(),
        'supplier_payment_term' : supplier_payment_term,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
