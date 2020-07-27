from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required
### DJANGO FORMS
from django.forms import inlineformset_factory
from django import forms

### SETTINGS:: ALL
from SETTINGS.models import *
from SETTINGS.forms import *
from SETTINGS.decorators import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings(request):
    return render(request, 'SETTINGS/settings/settings.html', {
        'company'                       : Company.objects.first(),
        'company_form'                  : CompanyModelForm(instance=Company.objects.first()),
        'supplier_types'                : SupplierType.objects.all(),
        'packing_types'                 : PackingType.objects.all(),
        'packing_materials'             : PackingMaterial.objects.all(),
        'purchase_order_statuses'       : PurchaseOrderStatus.objects.all(),
        'purchase_requisition_statuses' : PurchaseRequisitionStatus.objects.all(),
        'quotation_statuses'            : QuotationStatus.objects.all(),
        'sales_order_statuses'          : SalesOrderStatus.objects.all(),
        'daily_report_contact_methods'  : DailyReportContactMethod.objects.all(),
        'daily_report_types'            : DailyReportType.objects.all(),
        'living_arrangements'           : LivingArrangement.objects.all(),
        'races'                         : Race.objects.all(),
        'nationalities'                 : Nationality.objects.all(),
        'divisions'                     : Division.objects.all(),
        'departments'                   : Department.objects.all(),
        'sections'                      : Section.objects.all(),
        'positions'                     : Position.objects.all(),
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_company_create(request):
    if request.method == 'POST':
        form            = CompanyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = CompanyModelForm()

    return render(request, 'SETTINGS/settings/company/settings_company_create.html', {
        'company'           : Company.objects.first(),
        'form'              : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_company_update(request, id):
    try:
        company         = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Company ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = CompanyModelForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = CompanyModelForm(instance=company)
    
    return render(request, 'SETTINGS/settings/company/settings_company_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_supplier_type_create(request):
    if request.method == 'POST':
        form            = SupplierTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = SupplierTypeModelForm()
    
    return render(request, 'SETTINGS/settings/supplier/settings_supplier_type_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_supplier_type_update(request, id):
    try:
        supplier_type   = SupplierType.objects.get(id=id)
    except SupplierType.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Supplier Type ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = SupplierTypeModelForm(request.POST, instance=supplier_type)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = SupplierTypeModelForm(instance=supplier_type)

    return render(request, 'SETTINGS/settings/supplier/settings_supplier_type_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_packing_type_create(request):
    if request.method == 'POST':
        form            = PackingTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PackingTypeModelForm()

    return render(request, 'SETTINGS/settings/product/settings_packing_type_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_packing_type_update(request, id):
    try:
        packing_type    = PackingType.objects.get(id=id)
    except PackingType.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Packing Type ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = PackingTypeModelForm(request.POST, instance=packing_type)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PackingTypeModelForm(instance=packing_type)
    
    return render(request, 'SETTINGS/settings/product/settings_packing_type_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_packing_material_create(request):
    if request.method == 'POST':
        form            = PackingMaterialModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PackingMaterialModelForm()

    return render(request, 'SETTINGS/settings/product/settings_packing_material_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_packing_material_update(request, id):
    try:
        packing_material    = PackingMaterial.objects.get(id=id)
    except PackingMaterial.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Packing Materials ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = PackingMaterialModelForm(request.POST, instance=packing_material)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PackingMaterialModelForm(instance=packing_material)

    return render(request, 'SETTINGS/settings/product/settings_packing_material_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_purchase_order_status_create(request):
    if request.method == 'POST':
        form                = PurchaseOrderStatusModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PurchaseOrderStatusModelForm()

    return render(request, 'SETTINGS/settings/purchase_order/settings_purchase_order_status_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_purchase_order_status_update(request, id):
    try:
        purchase_order_status   = PurchaseOrderStatus.objects.get(id=id)
    except PurchaseOrderStatus.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Order Status ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = PurchaseOrderStatusModelForm(request.POST, instance=purchase_order_status)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PurchaseOrderStatusModelForm(instance=purchase_order_status)
    
    return render(request, 'SETTINGS/settings/purchase_order/settings_purchase_order_status_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_purchase_requisition_status_create(request):
    if request.method == 'POST':
        form            = PurchaseRequisitionStatusModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PurchaseRequisitionStatusModelForm()

    return render(request, 'SETTINGS/settings/purchase_requisition/settings_purchase_requisition_status_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_purchase_requisition_status_update(request, id):
    try:
        purchase_requisition_status   = PurchaseRequisitionStatus.objects.get(id=id)
    except PurchaseRequisitionStatus.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Purchase Requisition Status ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = PurchaseRequisitionStatusModelForm(request.POST, instance=purchase_requisition_status)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PurchaseRequisitionStatusModelForm(instance=purchase_requisition_status)
    
    return render(request, 'SETTINGS/settings/purchase_requisition/settings_purchase_requisition_status_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_quotation_status_create(request):
    if request.method == 'POST':
        form            = QuotationStatusModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = QuotationStatusModelForm()

    return render(request, 'SETTINGS/settings/quotation/settings_quotation_status_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_quotation_status_update(request, id):
    try:
        quotation_status   = QuotationStatus.objects.get(id=id)
    except QuotationStatus.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Quotation Status ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = QuotationStatusModelForm(request.POST, instance=quotation_status)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = QuotationStatusModelForm(instance=quotation_status)
    
    return render(request, 'SETTINGS/settings/quotation/settings_quotation_status_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_sales_order_status_create(request):
    if request.method == 'POST':
        form            = SalesOrderStatusModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = SalesOrderStatusModelForm()

    return render(request, 'SETTINGS/settings/sales_order/settings_sales_order_status_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_sales_order_status_update(request, id):
    try:
        sales_order_status   = SalesOrderStatus.objects.get(id=id)
    except SalesOrderStatus.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Sales Order Status ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = SalesOrderStatusModelForm(request.POST, instance=sales_order_status)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = SalesOrderStatusModelForm(instance=sales_order_status)
    
    return render(request, 'SETTINGS/settings/sales_order/settings_sales_order_status_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_daily_report_contact_method_create(request):
    if request.method == 'POST':
        form            = DailyReportContactMethodModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DailyReportContactMethodModelForm()

    return render(request, 'SETTINGS/settings/daily_report/settings_daily_report_contact_method_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_daily_report_contact_method_update(request, id):
    try:
        daily_report_contact_method   = DailyReportContactMethod.objects.get(id=id)
    except DailyReportContactMethod.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Daily Report Contact Method ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = DailyReportContactMethodModelForm(request.POST, instance=daily_report_contact_method)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DailyReportContactMethodModelForm(instance=daily_report_contact_method)
    
    return render(request, 'SETTINGS/settings/daily_report/settings_daily_report_contact_method_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_daily_report_type_create(request):
    if request.method == 'POST':
        form                = DailyReportTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DailyReportTypeModelForm()

    return render(request, 'SETTINGS/settings/daily_report/settings_daily_report_type_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_daily_report_type_update(request, id):
    try:
        daily_report_type   = DailyReportType.objects.get(id=id)
    except DailyReportType.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Daily Report Type ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = DailyReportTypeModelForm(request.POST, instance=daily_report_type)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DailyReportTypeModelForm(instance=daily_report_type)
    
    return render(request, 'SETTINGS/settings/daily_report/settings_daily_report_type_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_living_arrangement_create(request):
    if request.method == 'POST':
        form            = LivingArrangementModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = LivingArrangementModelForm()

    return render(request, 'SETTINGS/settings/employee/settings_living_arrangement_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_living_arrangement_update(request, id):
    try:
        living_arrangement      = LivingArrangement.objects.get(id=id)
    except LivingArrangement.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Living Arrangement ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = LivingArrangementModelForm(request.POST, instance=living_arrangement)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = LivingArrangementModelForm(instance=living_arrangement)
    
    return render(request, 'SETTINGS/settings/employee/settings_living_arrangement_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_race_create(request):
    if request.method == 'POST':
        form            = RaceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = RaceModelForm()

    return render(request, 'SETTINGS/settings/employee/settings_race_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_race_update(request, id):
    try:
        race            = Race.objects.get(id=id)
    except Race.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Race ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = RaceModelForm(request.POST, instance=race)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = RaceModelForm(instance=race)
    
    return render(request, 'SETTINGS/settings/employee/settings_race_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_nationality_create(request):
    if request.method == 'POST':
        form                = NationalityModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = NationalityModelForm()

    return render(request, 'SETTINGS/settings/employee/settings_nationality_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_nationality_update(request, id):
    try:
        nationality     = Nationality.objects.get(id=id)
    except Nationality.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Nationality ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = NationalityModelForm(request.POST, instance=nationality)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = NationalityModelForm(instance=nationality)
    
    return render(request, 'SETTINGS/settings/employee/settings_nationality_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_division_create(request):
    if request.method == 'POST':
        form            = DivisionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DivisionModelForm()

    return render(request, 'SETTINGS/settings/organization/settings_division_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_division_update(request, id):
    try:
        division        = Division.objects.get(id=id)
    except Division.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Division ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = DivisionModelForm(request.POST, instance=division)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DivisionModelForm(instance=division)
    
    return render(request, 'SETTINGS/settings/organization/settings_division_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_department_create(request):
    if request.method == 'POST':
        form                = DepartmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DepartmentModelForm()

    return render(request, 'SETTINGS/settings/organization/settings_department_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_department_update(request, id):
    try:
        department      = Department.objects.get(id=id)
    except Department.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Department ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = DepartmentModelForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = DepartmentModelForm(instance=department)
    
    return render(request, 'SETTINGS/settings/organization/settings_department_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_section_create(request):
    if request.method == 'POST':
        form                = SectionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = SectionModelForm()

    return render(request, 'SETTINGS/settings/organization/settings_section_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_section_update(request, id):
    try:
        section         = Section.objects.get(id=id)
    except Section.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Section ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = SectionModelForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = SectionModelForm(instance=section)
    
    return render(request, 'SETTINGS/settings/organization/settings_section_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_position_create(request):
    if request.method == 'POST':
        form                = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PositionModelForm()

    return render(request, 'SETTINGS/settings/organization/settings_position_create.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def settings_position_update(request, id):
    try:
        position        = Position.objects.get(id=id)
    except Position.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Position ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form            = PositionModelForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('SETTINGS:settings')
    else:
        form            = PositionModelForm(instance=position)
    
    return render(request, 'SETTINGS/settings/organization/settings_position_update.html', {
        'company'       : Company.objects.first(),
        'form'          : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
