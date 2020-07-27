from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required

### SETTINGS:: ALL
from SETTINGS.decorators import *
### WAREHOUSE:: ALL
from WAREHOUSE.models import *
from WAREHOUSE.forms import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def product_lot_number_list(request):
    product_lot_numbers   = ProductLotNumber.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            product_lot_numbers   = ProductLotNumber.objects.filter(
                Q(id__iexact                                = search_text) |
                Q(name__icontains                           = search_text) |
                Q(email__icontains                          = search_text) |
                Q(phone__icontains                          = search_text)
            )
        else:
            product_lot_numbers   = None
    
    return render(request, 'WAREHOUSE/product_lot_number/product_lot_number_list.html', {
        'company'               : Company.objects.first(),
        'product_lot_numbers'   : product_lot_numbers,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def product_lot_number_detail(request, id):
    try:
        product_lot_number      = ProductLotNumber.objects.get(id=id)
    except ProductLotNumber.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Product Lot Number : {} does not exist.'.format(id)})

    return render(request, 'WAREHOUSE/product_lot_number/product_lot_number_detail.html', {
        'company'               : Company.objects.first(),
        'product_lot_number'    : product_lot_number,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def product_lot_number_create(request):
    form        = ProductLotNumberModelForm()
    if request.method == 'POST':
        form    = ProductLotNumberModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_product_lot_number_id  = ProductLotNumber.objects.order_by('id').last().id
            return redirect('WAREHOUSE:product_lot_number_detail', id=last_product_lot_number_id)

    return render(request, 'WAREHOUSE/product_lot_number/product_lot_number/product_lot_number_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
# @login_required
# # @allow_users(allowed_departments=[])
# def product_lot_number_update(request):
