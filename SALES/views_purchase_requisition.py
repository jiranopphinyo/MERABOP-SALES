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
### SALES:: ALL
from SALES.models import *
from SALES.forms import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def purchase_requisition_list(request):
    purchase_requisitions   = PurchaseRequisitionItem.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            purchase_requisitions  = PurchaseRequisitionItem.objects.filter(
                Q(purchase_requisition__id__iexact                  = search_text) |
                Q(product__id__iexact                               = search_text) |
                Q(product__name__icontains                          = search_text)
            )
        else:
            purchase_requisitions  = None
    
    return render(request, 'SALES/purchase_requisition/purchase_requisition_list.html', {
        'company'               : Company.objects.first(),
        'purchase_requisitions' : purchase_requisitions,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_detail(request, id):
    try:
        purchase_requisition            = PurchaseRequisition.objects.get(id=id)
    except PurchaseRequisition.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requisition ID : {} does not exist.'.format(id)})

    purchase_requisition_items          = PurchaseRequisitionItem.objects.filter(purchase_requisition=id)
    purchase_requisition_status         = PurchaseRequisitionStatus.objects.all()
    purchase_requisition_status_logs    = PurchaseRequisitionStatusLog.objects.filter(purchase_requisition=id).order_by('created_at')

    last_status_log     = purchase_requisition_status_logs.last()
    len_status_log      = purchase_requisition_status_logs.count()
    len_status          = purchase_requisition_status.count()

    if len_status_log:
        percent         = round((((len_status_log - 1) / (len_status - 1)) * 100), 2)
    else:
        percent         = 0

    form                = PurchaseRequisitionStatusLogModelForm(initial={'purchase_requisition': purchase_requisition, 'user': request.user.get_full_name()})
    if request.method == 'POST':
        form            = PurchaseRequisitionStatusLogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:purchase_requisition_detail', id=id)

    return render(request, 'SALES/purchase_requisition/purchase_requisition_detail.html', {
        'company'               : Company.objects.first(),
        'purchase_requisition'             : purchase_requisition,
        'purchase_requisition_items'       : purchase_requisition_items,
        'purchase_requisition_status'      : purchase_requisition_status,
        'purchase_requisition_status_logs' : purchase_requisition_status_logs,
        'last_status_log'       : last_status_log,
        'form'                  : form,
        'percent'               : percent,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def purchase_requisition_print(request, id):
    try:
        purchase_requisition    = PurchaseRequisition.objects.get(id=id)
    except PurchaseRequisition.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requisition ID : {} does not exist.'.format(id)})
    
    purchase_requisition_items  = PurchaseRequisitionItem.objects.filter(purchase_requisition=id)

    return render(request, 'SALES/purchase_requisition/purchase_requisition_print.html', {
        'company'               : Company.objects.first(),
        'purchase_requisition'           : purchase_requisition,
        'purchase_requisition_items'     : purchase_requisition_items,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_create(request):
    form                = PurchaseRequisitionModelForm()
    if request.method == 'POST':
        form            = PurchaseRequisitionModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_purchase_requisition_id    = PurchaseRequisition.objects.order_by('id').last().id

            try:
                status  = PurchaseRequisitionStatus.objects.get(id=1)
            except PurchaseRequisitionStatus.DoesNotExist:
                PurchaseRequisitionStatus.objects.create(purchase_requisition_status="Created")
                status  = PurchaseRequisitionStatus.objects.get(id=1)
            PurchaseRequisitionStatusLog.objects.create(purchase_requisition=PurchaseRequisition.objects.get(id=last_purchase_requisition_id), status=status, user=request.user.get_full_name(), remark="Auto create status log.")

            return redirect('SALES:purchase_requisition_item_create', id=last_purchase_requisition_id)

    return render(request, 'SALES/purchase_requisition/purchase_requisition/purchase_requisition_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_update_before_create(request, id):
    try:
        purchase_requisition     = PurchaseRequisition.objects.get(id=id)
    except PurchaseRequisition.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requisition ID : {} does not exist.'.format(id)})

    form                = PurchaseRequisitionModelForm(instance=purchase_requisition)
    if request.method == 'POST':
        form            = PurchaseRequisitionModelForm(request.POST, instance=purchase_requisition)
        if form.is_valid():
            form.save()
            return redirect('SALES:purchase_requisition_item_create', id=id)
    
    return render(request, 'SALES/purchase_requisition/purchase_requisition/purchase_requisition_update_before_create.html', {
        'company'               : Company.objects.first(),
        'purchase_requisition'  : purchase_requisition,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_update_after_create(request, id):
    try:
        purchase_requisition     = PurchaseRequisition.objects.get(id=id)
    except PurchaseRequisition.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requisition ID : {} does not exist.'.format(id)})

    form                = PurchaseRequisitionModelForm(instance=purchase_requisition)
    if request.method == 'POST':
        form            = PurchaseRequisitionModelForm(request.POST, instance=purchase_requisition)
        if form.is_valid():
            form.save()
            return redirect('SALES:purchase_requisition_detail', id=id)
    
    return render(request, 'SALES/purchase_requisition/purchase_requisition/purchase_requisition_update_after_create.html', {
        'company'               : Company.objects.first(),
        'purchase_requisition'  : purchase_requisition,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_item_create(request, id):
    try:
        purchase_requisition     = PurchaseRequisition.objects.get(id=id)
    except PurchaseRequisition.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order ID : {} does not exist.'.format(id)})
    
    PurchaseRequisitionItemInlineFormSet = inlineformset_factory(
                                    PurchaseRequisition,
                                    PurchaseRequisitionItem,
                                    extra   = 3,
                                    fields  = ('product', 'quantity', 'unit_price', 'remark'),
                                    widgets = {
                                        'product'   : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
                                        'quantity'  : forms.NumberInput(attrs={'class': 'form-control'}),
                                        'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
                                        'remark'    : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
                                    })
    formset             = PurchaseRequisitionItemInlineFormSet(instance=purchase_requisition)

    if request.method == 'POST':
        formset         = PurchaseRequisitionItemInlineFormSet(request.POST, instance=purchase_requisition)
        if formset.is_valid():
            formset.save()
            return redirect('SALES:purchase_requisition_detail', id=id)
    
    return render(request, 'SALES/purchase_requisition/item/purchase_requisition_item_create.html', {
        'company'               : Company.objects.first(),
        'purchase_requisition'  : purchase_requisition,
        'formset'               : formset,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_item_create_after_create(request, id):
    try:
        purchase_requisition     = PurchaseRequisition.objects.get(id=id)
    except PurchaseRequisition.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requisition ID : {} does not exist.'.format(id)})

    form                = PurchaseRequisitionItemModelForm(initial={'purchase_requisition': purchase_requisition})
    if request.method == 'POST':
        form            = PurchaseRequisitionItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:purchase_requisition_detail', id=id)
    
    return render(request, 'SALES/purchase_requisition/item/purchase_requisition_item_create_after_create.html', {
        'company'               : Company.objects.first(),
        'purchase_requisition'  : purchase_requisition,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_item_update(request, id):
    try:
        purchase_requisition_item   = PurchaseRequisitionItem.objects.get(id=id)
    except PurchaseRequisitionItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requsitiion Item ID : {} does not exist.'.format(id)})
    
    form                    = PurchaseRequisitionItemModelForm(instance=purchase_requisition_item)
    if request.method == 'POST':
        form                = PurchaseRequisitionItemModelForm(request.POST, instance=purchase_requisition_item)
        if form.is_valid():
            form.save()
            return redirect('SALES:purchase_requisition_detail', id=form.cleaned_data['purchase_requisition'].id)

    return render(request, 'SALES/purchase_requisition/item/purchase_requisition_item_update.html', {
        'company'                   : Company.objects.first(),
        'purchase_requisition_item' : purchase_requisition_item,
        'form'                      : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def purchase_requisition_item_delete(request, id):
    try:
        purchase_requisition_item   = PurchaseRequisitionItem.objects.get(id=id)
        purchase_requisition        = PurchaseRequisition.objects.get(id=purchase_requisition_item.purchase_requisition.id)
    except PurchaseRequisitionItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requisition Item ID : {} does not exist.'.format(id)})
    
    if request.method == 'POST':
        purchase_requisition_item.delete()
        purchase_requisition.save()
        return redirect('SALES:purchase_requisition_detail', id=purchase_requisition_item.purchase_requisition.id)

    return render(request, 'SALES/purchase_requisition/item/purchase_requisition_item_delete.html', {
        'company'                   : Company.objects.first(),
        'purchase_requisition_item' : purchase_requisition_item,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
