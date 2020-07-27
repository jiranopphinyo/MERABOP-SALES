from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required

### SETTINGS:: ALL
from SETTINGS.decorators import *
### PURCHASE:: ALL
from PURCHASE.models import *
from PURCHASE.forms import *
### WAREHOUSE:: ALL
from WAREHOUSE.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def product_list(request):
    products            = Product.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            products    = Product.objects.filter(
                Q(id                                        = search_text) |
                Q(name__icontains                           = search_text) |
                Q(supplier__name__icontains                 = search_text)
            )
        else:
            products    = None
    
    return render(request, 'PURCHASE/product/product_list.html', {
        'company'   : Company.objects.first(),
        'products'  : products,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def product_detail(request, id):
    try:
        product         = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Product ID : {} does not exist.'.format(id)})

    product_lot_numbers = ProductLotNumber.objects.filter(product=id)

    return render(request, 'PURCHASE/product/product_detail.html', {
        'company'               : Company.objects.first(),
        'product'               : product,
        'product_lot_numbers'   : product_lot_numbers,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def product_create(request):
    form        = ProductModelForm()
    if request.method == 'POST':
        form    = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:product_detail', id=form.cleaned_data['id'])

    return render(request, 'PURCHASE/product/general/product_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def product_update(request, id):
    try:
        product     = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Product ID : {} does not exist.'.format(id)})
    
    form            = ProductModelForm(instance=product)
    if request.method == 'POST':
        form        = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:product_detail', id=id)

    return render(request, 'PURCHASE/product/general/product_update.html', {
        'company'               : Company.objects.first(),
        'product'               : product,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
