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
def quotation_list(request):
    quotations          = Quotation.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            quotations  = Quotation.objects.filter(
                Q(sales_reps__first_name__iexact             = search_text) |
                Q(customer__id__iexact                       = search_text) |
                Q(customer__name__icontains                  = search_text)
            )
        else:
            quotations  = None
    
    return render(request, 'SALES/quotation/quotation_list.html', {
        'company'           : Company.objects.first(),
        'quotations'        : quotations,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_detail(request, id):
    try:
        quotation       = Quotation.objects.get(id=id)
    except Quotation.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation ID : {} does not exist.'.format(id)})

    quotation_items     = QuotationItem.objects.filter(quotation=id)
    quotation_status    = QuotationStatus.objects.all()
    quotation_status_logs= QuotationStatusLog.objects.filter(quotation=id).order_by('created_at')

    last_status_log     = quotation_status_logs.last()
    len_status_log      = quotation_status_logs.count()
    len_status          = quotation_status.count()

    if len_status_log:
        percent         = round((((len_status_log - 1) / (len_status - 1)) * 100), 2)
    else:
        percent         = 0

    form                = QuotationStatusLogModelForm(initial={'quotation': quotation, 'user': request.user.get_full_name()})
    if request.method == 'POST':
        form            = QuotationStatusLogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:quotation_detail', id=id)

    return render(request, 'SALES/quotation/quotation_detail.html', {
        'company'               : Company.objects.first(),
        'quotation'             : quotation,
        'quotation_items'       : quotation_items,
        'quotation_status'      : quotation_status,
        'quotation_status_logs' : quotation_status_logs,
        'last_status_log'       : last_status_log,
        'form'                  : form,
        'percent'               : percent,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_print(request, id):
    try:
        quotation       = Quotation.objects.get(id=id)
    except Quotation.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation ID : {} does not exist.'.format(id)})
    
    quotation_items     = QuotationItem.objects.filter(quotation=id)

    return render(request, 'SALES/quotation/quotation_print.html', {
        'company'               : Company.objects.first(),
        'quotation'             : quotation,
        'quotation_items'       : quotation_items,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_create(request):
    form                = QuotationModelForm()
    if request.method == 'POST':
        form            = QuotationModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_quotation_id    = Quotation.objects.order_by('id').last().id

            try:
                status  = QuotationStatus.objects.get(id=1)
            except QuotationStatus.DoesNotExist:
                QuotationStatus.objects.create(quotation_status="Created")
                status  = QuotationStatus.objects.get(id=1)
            QuotationStatusLog.objects.create(quotation=Quotation.objects.get(id=last_quotation_id), status=status, user=request.user.get_full_name(), remark="Auto create status log.")

            return redirect('SALES:quotation_item_create', id=last_quotation_id)

    return render(request, 'SALES/quotation/quotation/quotation_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_update_before_create(request, id):
    try:
        quotation       = Quotation.objects.get(id=id)
    except Quotation.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation ID : {} does not exist.'.format(id)})

    form                = QuotationModelForm(instance=quotation)
    if request.method == 'POST':
        form            = QuotationModelForm(request.POST, instance=quotation)
        if form.is_valid():
            form.save()
            return redirect('SALES:quotation_item_create', id=id)
    
    return render(request, 'SALES/quotation/quotation/quotation_update_before_create.html', {
        'company'               : Company.objects.first(),
        'quotation'             : quotation,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_update_after_create(request, id):
    try:
        quotation       = Quotation.objects.get(id=id)
    except Quotation.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation ID : {} does not exist.'.format(id)})

    form                = QuotationModelForm(instance=quotation)
    if request.method == 'POST':
        form            = QuotationModelForm(request.POST, instance=quotation)
        if form.is_valid():
            form.save()
            return redirect('SALES:quotation_detail', id=id)
    
    return render(request, 'SALES/quotation/quotation/quotation_update_after_create.html', {
        'company'               : Company.objects.first(),
        'quotation'             : quotation,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_item_create(request, id):
    try:
        quotation       = Quotation.objects.get(id=id)
    except Quotation.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation ID : {} does not exist.'.format(id)})
    
    QuotationItemInlineFormSet = inlineformset_factory(
                                    Quotation,
                                    QuotationItem,
                                    extra   = 3,
                                    fields  = ('product', 'quantity', 'unit_price'),
                                    widgets = {
                                        'product'   : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
                                        'quantity'  : forms.NumberInput(attrs={'class': 'form-control'}),
                                        'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
                                    })
    formset             = QuotationItemInlineFormSet(instance=quotation)

    if request.method == 'POST':
        formset         = QuotationItemInlineFormSet(request.POST, instance=quotation)
        if formset.is_valid():
            formset.save()
            return redirect('SALES:quotation_detail', id=id)
    
    return render(request, 'SALES/quotation/item/quotation_item_create.html', {
        'company'       : Company.objects.first(),
        'quotation'     : quotation,
        'formset'       : formset,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_item_create_after_create(request, id):
    try:
        quotation       = Quotation.objects.get(id=id)
    except Quotation.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation ID : {} does not exist.'.format(id)})

    form                = QuotationItemModelForm(initial={'quotation': quotation})
    if request.method == 'POST':
        form            = QuotationItemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:quotation_detail', id=id)
    
    return render(request, 'SALES/quotation/item/quotation_item_create_after_create.html', {
        'company'       : Company.objects.first(),
        'quotation'     : quotation,
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_item_update(request, id):
    try:
        quotation_item      = QuotationItem.objects.get(id=id)
    except QuotationItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation Item ID : {} does not exist.'.format(id)})
    
    form                    = QuotationItemModelForm(instance=quotation_item)
    if request.method == 'POST':
        form                = QuotationItemModelForm(request.POST, instance=quotation_item)
        if form.is_valid():
            form.save()
            return redirect('SALES:quotation_detail', id=form.cleaned_data['quotation'].id)

    return render(request, 'SALES/quotation/item/quotation_item_update.html', {
        'company'               : Company.objects.first(),
        'quotation_item'        : quotation_item,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def quotation_item_delete(request, id):
    try:
        quotation_item      = QuotationItem.objects.get(id=id)
        quotation           = Quotation.objects.get(id=quotation_item.quotation.id)
    except QuotationItem.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation Item ID : {} does not exist.'.format(id)})
    
    if request.method == 'POST':
        quotation_item.delete()
        quotation.save()
        return redirect('SALES:quotation_detail', id=quotation_item.quotation.id)

    return render(request, 'SALES/quotation/item/quotation_item_delete.html', {
        'company'               : Company.objects.first(),
        'quotation_item'        : quotation_item,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
