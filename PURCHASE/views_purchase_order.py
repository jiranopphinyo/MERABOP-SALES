from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required
### DJANGO FORMS
from django.forms import inlineformset_factory
from django import forms

### SETTINGS:: ALL
from SETTINGS.models import *
from SETTINGS.decorators import *
### PURCHASE:: ALL
from PURCHASE.models import *
from PURCHASE.forms import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def purchase_order_list(request):
    purchase_orders     = PurchaseOrderItem.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            purchase_orders  = PurchaseOrderItem.objects.filter(
                Q(purchase_order__supplier__id__iexact          = search_text) |
                Q(purchase_order__supplier__name__icontains     = search_text) |
                Q(product__id__iexact                           = search_text) |
                Q(product__name__icontains                      = search_text)
            )
        else:
            purchase_orders  = None
    
    return render(request, 'PURCHASE/purchase_order/purchase_order_list.html', {
        'company'           : Company.objects.first(),
        'purchase_orders'   : purchase_orders,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_detail(request, id):
    try:
        purchase_order       = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order ID : {} does not exist.'.format(id)})

    purchase_order_items     = PurchaseOrderItem.objects.filter(purchase_order=id)
    purchase_order_status    = PurchaseOrderStatus.objects.all()
    purchase_order_status_logs= PurchaseOrderStatusLog.objects.filter(purchase_order=id).order_by('created_at')

    last_status_log     = purchase_order_status_logs.last()
    len_status_log      = purchase_order_status_logs.count()
    len_status          = purchase_order_status.count()

    if len_status_log:
        percent         = round((((len_status_log - 1) / (len_status - 1)) * 100), 2)
    else:
        percent         = 0

    form                = PurchaseOrderStatusLogModelForm(initial={'purchase_order': purchase_order, 'user': request.user.get_full_name()})
    if request.method == 'POST':
        form            = PurchaseOrderStatusLogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:purchase_order_detail', id=id)

    return render(request, 'PURCHASE/purchase_order/purchase_order_detail.html', {
        'company'                       : Company.objects.first(),
        'purchase_order'                : purchase_order,
        'purchase_order_items'          : purchase_order_items,
        'purchase_order_status'         : purchase_order_status,
        'purchase_order_status_logs'    : purchase_order_status_logs,
        'last_status_log'               : last_status_log,
        'form'                          : form,
        'percent'                       : percent,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def purchase_order_print(request, id):
    try:
        purchase_order      = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order ID : {} does not exist.'.format(id)})
    
    purchase_order_items    = PurchaseOrderItem.objects.filter(purchase_order=id)

    return render(request, 'PURCHASE/purchase_order/purchase_order_print.html', {
        'company'                   : Company.objects.first(),
        'purchase_order'            : purchase_order,
        'purchase_order_items'      : purchase_order_items,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_create(request):
    form                = PurchaseOrderModelForm()
    if request.method == 'POST':
        form            = PurchaseOrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_purchase_order_id    = PurchaseOrder.objects.order_by('id').last().id

            try:
                status  = PurchaseOrderStatus.objects.get(id=1)
            except PurchaseOrderStatus.DoesNotExist:
                PurchaseOrderStatus.objects.create(purchase_order_status="Created")
                status  = PurchaseOrderStatus.objects.get(id=1)
            PurchaseOrderStatusLog.objects.create(purchase_order=PurchaseOrder.objects.get(id=last_purchase_order_id), status=status, user=request.user.get_full_name(), remark="Auto create status log.")

            return redirect('PURCHASE:purchase_order_item_create', id=last_purchase_order_id)

    return render(request, 'PURCHASE/purchase_order/purchase_order/purchase_order_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_update_before_create(request, id):
    try:
        purchase_order  = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order ID : {} does not exist.'.format(id)})

    form                = PurchaseOrderModelForm(instance=purchase_order)
    if request.method == 'POST':
        form            = PurchaseOrderModelForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:purchase_order_item_create', id=id)
    
    return render(request, 'PURCHASE/purchase_order/purchase_order/purchase_order_update_before_create.html', {
        'company'               : Company.objects.first(),
        'purchase_order'        : purchase_order,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_update_after_create(request, id):
    try:
        purchase_order  = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order ID : {} does not exist.'.format(id)})

    form                = PurchaseOrderModelForm(instance=purchase_order)
    if request.method == 'POST':
        form            = PurchaseOrderModelForm(request.POST, instance=purchase_order)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:purchase_order_detail', id=id)
    
    return render(request, 'PURCHASE/purchase_order/purchase_order/purchase_order_update_after_create.html', {
        'company'               : Company.objects.first(),
        'purchase_order'        : purchase_order,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_item_create(request, id):
    try:
        purchase_order  = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order ID : {} does not exist.'.format(id)})
    
    PurchaseOrderItemInlineFormSet = inlineformset_factory(
                                    PurchaseOrder,
                                    PurchaseOrderItem,
                                    extra   = 3,
                                    fields  = ('product', 'quantity', 'unit_price'),
                                    widgets = {
                                        'product'   : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
                                        'quantity'  : forms.NumberInput(attrs={'class': 'form-control'}),
                                        'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
                                    })
    formset             = PurchaseOrderItemInlineFormSet(instance=purchase_order)

    if request.method == 'POST':
        formset         = PurchaseOrderItemInlineFormSet(request.POST, instance=purchase_order)
        if formset.is_valid():
            formset.save()
            return redirect('PURCHASE:purchase_order_detail', id=id)
    
    return render(request, 'PURCHASE/purchase_order/item/purchase_order_item_create.html', {
        'company'           : Company.objects.first(),
        'purchase_order'    : purchase_order,
        'formset'           : formset,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_item_create_after_create(request, id):
    try:
        purchase_order  = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order ID : {} does not exist.'.format(id)})

    form                = PurchaseOrderItemModelForm(initial={'purchase_order': purchase_order})
    if request.method == 'POST':
        form            = PurchaseOrderItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:purchase_order_detail', id=id)
    
    return render(request, 'PURCHASE/purchase_order/item/purchase_order_item_create_after_create.html', {
        'company'           : Company.objects.first(),
        'purchase_order'    : purchase_order,
        'form'              : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_item_update(request, id):
    try:
        purchase_order_item = PurchaseOrderItem.objects.get(id=id)
    except PurchaseOrderItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order Item ID : {} does not exist.'.format(id)})
    
    form                    = PurchaseOrderItemModelForm(instance=purchase_order_item)
    if request.method == 'POST':
        form                = PurchaseOrderItemModelForm(request.POST, instance=purchase_order_item)
        if form.is_valid():
            form.save()
            return redirect('PURCHASE:purchase_order_detail', id=form.cleaned_data['purchase_order'].id)

    return render(request, 'PURCHASE/purchase_order/item/purchase_order_item_update.html', {
        'company'               : Company.objects.first(),
        'purchase_order_item'   : purchase_order_item,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_order_item_delete(request, id):
    try:
        purchase_order_item = PurchaseOrderItem.objects.get(id=id)
        purchase_order      = PurchaseOrder.objects.get(id=purchase_order_item.purchase_order.id)
    except PurchaseOrderItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order Item ID : {} does not exist.'.format(id)})
    
    if request.method == 'POST':
        purchase_order_item.delete()
        purchase_order.save()
        return redirect('PURCHASE:purchase_order_detail', id=purchase_order_item.purchase_order.id)

    return render(request, 'PURCHASE/purchase_order/item/purchase_order_item_delete.html', {
        'company'               : Company.objects.first(),
        'purchase_order_item'   : purchase_order_item,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
