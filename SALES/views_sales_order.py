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
def sales_order_list(request):
    sales_orders    = SalesOrder.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            sales_orders  = SalesOrder.objects.filter(
                Q(sales_reps__first_name__iexact             = search_text) |
                Q(customer__id__iexact                       = search_text) |
                Q(customer__name__icontains                  = search_text)
            )
        else:
            sales_orders  = None
    
    return render(request, 'SALES/sales_order/sales_order_list.html', {
        'company'           : Company.objects.first(),
        'sales_orders'      : sales_orders,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_detail(request, id):
    try:
        sales_order       = SalesOrder.objects.get(id=id)
    except SalesOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order ID : {} does not exist.'.format(id)})

    sales_order_items     = SalesOrderItem.objects.filter(sales_order=id)
    sales_order_status    = SalesOrderStatus.objects.all()
    sales_order_status_logs= SalesOrderStatusLog.objects.filter(sales_order=id).order_by('created_at')

    last_status_log     = sales_order_status_logs.last()
    len_status_log      = sales_order_status_logs.count()
    len_status          = sales_order_status.count()

    if len_status_log:
        percent         = round((((len_status_log - 1) / (len_status - 1)) * 100), 2)
    else:
        percent         = 0

    form                = SalesOrderStatusLogModelForm(initial={'sales_order': sales_order, 'user': request.user.get_full_name()})
    if request.method == 'POST':
        form            = SalesOrderStatusLogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:sales_order_detail', id=id)

    return render(request, 'SALES/sales_order/sales_order_detail.html', {
        'company'               : Company.objects.first(),
        'sales_order'             : sales_order,
        'sales_order_items'       : sales_order_items,
        'sales_order_status'      : sales_order_status,
        'sales_order_status_logs' : sales_order_status_logs,
        'last_status_log'       : last_status_log,
        'form'                  : form,
        'percent'               : percent,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def sales_order_print(request, id):
    try:
        sales_order     = SalesOrder.objects.get(id=id)
    except SalesOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order ID : {} does not exist.'.format(id)})
    
    sales_order_items   = SalesOrderItem.objects.filter(sales_order=id)

    return render(request, 'SALES/sales_order/sales_order_print.html', {
        'company'               : Company.objects.first(),
        'sales_order'           : sales_order,
        'sales_order_items'     : sales_order_items,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_create(request):
    form                = SalesOrderModelForm()
    if request.method == 'POST':
        form            = SalesOrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_sales_order_id    = SalesOrder.objects.order_by('id').last().id

            try:
                status  = SalesOrderStatus.objects.get(id=1)
            except SalesOrderStatus.DoesNotExist:
                SalesOrderStatus.objects.create(sales_order_status="Created")
                status  = SalesOrderStatus.objects.get(id=1)
            SalesOrderStatusLog.objects.create(sales_order=SalesOrder.objects.get(id=last_sales_order_id), status=status, user=request.user.get_full_name(), remark="Auto create status log.")

            return redirect('SALES:sales_order_item_create', id=last_sales_order_id)

    return render(request, 'SALES/sales_order/sales_order/sales_order_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_update_before_create(request, id):
    try:
        sales_order     = SalesOrder.objects.get(id=id)
    except SalesOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order ID : {} does not exist.'.format(id)})

    form                = SalesOrderModelForm(instance=sales_order)
    if request.method == 'POST':
        form            = SalesOrderModelForm(request.POST, instance=sales_order)
        if form.is_valid():
            form.save()
            return redirect('SALES:sales_order_item_create', id=id)
    
    return render(request, 'SALES/sales_order/sales_order/sales_order_update_before_create.html', {
        'company'               : Company.objects.first(),
        'sales_order'           : sales_order,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_update_after_create(request, id):
    try:
        sales_order     = SalesOrder.objects.get(id=id)
    except SalesOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order ID : {} does not exist.'.format(id)})

    form                = SalesOrderModelForm(instance=sales_order)
    if request.method == 'POST':
        form            = SalesOrderModelForm(request.POST, instance=sales_order)
        if form.is_valid():
            form.save()
            return redirect('SALES:sales_order_detail', id=id)
    
    return render(request, 'SALES/sales_order/sales_order/sales_order_update_after_create.html', {
        'company'               : Company.objects.first(),
        'sales_order'           : sales_order,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_item_create(request, id):
    try:
        sales_order     = SalesOrder.objects.get(id=id)
    except SalesOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order ID : {} does not exist.'.format(id)})
    
    SalesOrderItemInlineFormSet = inlineformset_factory(
                                    SalesOrder,
                                    SalesOrderItem,
                                    extra   = 3,
                                    fields  = ('product', 'quantity', 'unit_price'),
                                    widgets = {
                                        'product'   : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
                                        'quantity'  : forms.NumberInput(attrs={'class': 'form-control'}),
                                        'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
                                    })
    formset             = SalesOrderItemInlineFormSet(instance=sales_order)

    if request.method == 'POST':
        formset         = SalesOrderItemInlineFormSet(request.POST, instance=sales_order)
        if formset.is_valid():
            formset.save()
            return redirect('SALES:sales_order_detail', id=id)
    
    return render(request, 'SALES/sales_order/item/sales_order_item_create.html', {
        'company'       : Company.objects.first(),
        'sales_order'   : sales_order,
        'formset'       : formset,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_item_create_after_create(request, id):
    try:
        sales_order     = SalesOrder.objects.get(id=id)
    except SalesOrder.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order ID : {} does not exist.'.format(id)})

    form                = SalesOrderItemModelForm(initial={'sales_order': sales_order})
    if request.method == 'POST':
        form            = SalesOrderItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:sales_order_detail', id=id)
    
    return render(request, 'SALES/sales_order/item/sales_order_item_create_after_create.html', {
        'company'       : Company.objects.first(),
        'sales_order'   : sales_order,
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_item_update(request, id):
    try:
        sales_order_item    = SalesOrderItem.objects.get(id=id)
    except SalesOrderItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order Item ID : {} does not exist.'.format(id)})
    
    form                    = SalesOrderItemModelForm(instance=sales_order_item)
    if request.method == 'POST':
        form                = SalesOrderItemModelForm(request.POST, instance=sales_order_item)
        if form.is_valid():
            form.save()
            return redirect('SALES:sales_order_detail', id=form.cleaned_data['sales_order'].id)

    return render(request, 'SALES/sales_order/item/sales_order_item_update.html', {
        'company'               : Company.objects.first(),
        'sales_order_item'      : sales_order_item,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def sales_order_item_delete(request, id):
    try:
        sales_order_item    = SalesOrderItem.objects.get(id=id)
        sales_order         = SalesOrder.objects.get(id=sales_order_item.sales_order.id)
    except SalesOrderItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order Item ID : {} does not exist.'.format(id)})
    
    if request.method == 'POST':
        sales_order_item.delete()
        sales_order.save()
        return redirect('SALES:sales_order_detail', id=sales_order_item.sales_order.id)

    return render(request, 'SALES/sales_order/item/sales_order_item_delete.html', {
        'company'               : Company.objects.first(),
        'sales_order_item'      : sales_order_item,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
