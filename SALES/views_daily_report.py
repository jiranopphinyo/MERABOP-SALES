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
def daily_report_list(request):
    daily_reports    = DailyReportItem.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            daily_reports  = DailyReportItem.objects.filter(
                Q(daily_report__sales_reps__first_name__iexact      = search_text) |
                Q(daily_report__customer__customer__id__iexact      = search_text) |
                Q(daily_report__customer__customer__name__icontains = search_text) |
                Q(daily_report__customer_contact_person__fullname__icontains = search_text) |
                Q(product__id__iexact                               = search_text) |
                Q(product__name__icontains                          = search_text)
            )
        else:
            daily_reports  = None
    
    return render(request, 'SALES/daily_report/daily_report_list.html', {
        'company'           : Company.objects.first(),
        'daily_reports'     : daily_reports,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def daily_report_detail(request, id):
    try:
        daily_report        = DailyReport.objects.get(id=id)
    except DailyReport.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Daily Report ID : {} does not exist.'.format(id)})

    daily_report_items      = DailyReportItem.objects.filter(daily_report=id)
    daily_report_type       = DailyReportType.objects.all()

    return render(request, 'SALES/daily_report/daily_report_detail.html', {
        'company'               : Company.objects.first(),
        'daily_report'          : daily_report,
        'daily_report_items'    : daily_report_items,
        'daily_report_type'     : daily_report_type,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def daily_report_create(request):
    form                = DailyReportModelForm()
    if request.method == 'POST':
        form            = DailyReportModelForm(request.POST)
        if form.is_valid():
            form.save()
            last_daily_report_id    = DailyReport.objects.order_by('id').last().id
            return redirect('SALES:daily_report_item_create', id=last_daily_report_id)

    return render(request, 'SALES/daily_report/daily_report/daily_report_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def daily_report_update_before_create(request, id):
    try:
        daily_report     = DailyReport.objects.get(id=id)
    except DailyReport.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Daily Report ID : {} does not exist.'.format(id)})

    form                = DailyReportModelForm(instance=daily_report)
    if request.method == 'POST':
        form            = DailyReportModelForm(request.POST, instance=daily_report)
        if form.is_valid():
            form.save()
            return redirect('SALES:daily_report_item_create', id=id)
    
    return render(request, 'SALES/daily_report/daily_report/daily_report_update_before_create.html', {
        'company'               : Company.objects.first(),
        'daily_report'          : daily_report,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def daily_report_update_after_create(request, id):
    try:
        daily_report    = DailyReport.objects.get(id=id)
    except DailyReport.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Daily Report ID : {} does not exist.'.format(id)})

    form                = DailyReportModelForm(instance=daily_report)
    if request.method == 'POST':
        form            = DailyReportModelForm(request.POST, instance=daily_report)
        if form.is_valid():
            form.save()
            return redirect('SALES:daily_report_list')
    
    return render(request, 'SALES/daily_report/daily_report/daily_report_update_after_create.html', {
        'company'               : Company.objects.first(),
        'daily_report'          : daily_report,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def daily_report_item_create(request, id):
    try:
        daily_report     = DailyReport.objects.get(id=id)
    except DailyReport.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Daily Report ID : {} does not exist.'.format(id)})
    
    DailyReportItemInlineFormSet = inlineformset_factory(
                                    DailyReport,
                                    DailyReportItem,
                                    extra   = 3,
                                    fields  = ('product', 'daily_report_type', 'quantity', 'unit_price', 'is_accept', 'remark'),
                                    widgets = {
                                        'product'           : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
                                        'daily_report_type' : forms.Select(attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
                                        'quantity'          : forms.NumberInput(attrs={'class': 'form-control'}),
                                        'unit_price'        : forms.NumberInput(attrs={'class': 'form-control'}),
                                        'is_accept'         : forms.Select(choices=((True, "Yes"), (False, "No"), (None, "Unknown")), attrs={'class': 'select2 form-control', 'data-toggle': 'select2'}),
                                        'remark'            : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
                                    })
    formset             = DailyReportItemInlineFormSet(instance=daily_report)

    if request.method == 'POST':
        formset         = DailyReportItemInlineFormSet(request.POST, instance=daily_report)
        if formset.is_valid():
            formset.save()
            return redirect('SALES:daily_report_list')
    
    return render(request, 'SALES/daily_report/item/daily_report_item_create.html', {
        'company'       : Company.objects.first(),
        'daily_report'  : daily_report,
        'formset'       : formset,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
