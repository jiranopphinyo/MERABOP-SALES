from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required

### SETTINGS:: ALL
from SETTINGS.decorators import *
### HUMANRESOURCE:: ALL
from HUMANRESOURCE.models import *
from HUMANRESOURCE.forms import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def employee_list(request):
    employees   = EmployeePersonalInfo.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            employees   = EmployeePersonalInfo.objects.filter(
                Q(employee__first_name__icontains       = search_text) |
                Q(employee__last_name__icontains        = search_text) |
                Q(race__race__iexact                    = search_text) |
                Q(nationality__nationality__iexact      = search_text) |
                Q(religion__icontains                   = search_text) |
                Q(blood_group__icontains                = search_text) |
                Q(gender__gender__iexact                = search_text) |
                Q(email__icontains                      = search_text) |
                Q(phone__icontains                      = search_text)
            )
        else:
            employees   = None
    
    return render(request, 'HUMANRESOURCE/employee/employee_list.html', {
        'company'   : Company.objects.first(),
        'employees' : employees,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def employee_detail(request, id):
    try:
        employee        = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Employee ID : {} does not exist.'.format(id)})

    personal            = EmployeePersonalInfo.objects.get(employee=employee)
    addresses           = EmployeeAddress.objects.filter(employee=employee)

    return render(request, 'HUMANRESOURCE/employee/employee_detail.html', {
        'company'               : Company.objects.first(),
        'employee'              : employee,
        'personal'              : personal,
        'addresses'             : addresses,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def employee_create(request):
    if request.method == 'POST':
        form    = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            Employee.objects.create(
                user            = form.instance,
                first_name      = form.cleaned_data['first_name'],
                last_name       = form.cleaned_data['last_name'],
            )
            last_employee_id    = Employee.objects.order_by('created_at').last().id
            return redirect('HUMANRESOURCE:employee_personal_create', id=last_employee_id)
    else:
        form    = UserModelForm()

    return render(request, 'HUMANRESOURCE/employee/general/employee_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def employee_update(request, id):
    try:
        employee    = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Employee ID : {} does not exist.'.format(id)})
    
    form            = EmployeeModelForm(instance=employee)
    if request.method == 'POST':
        form        = EmployeeModelForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('HUMANRESOURCE:employee_detail', id=id)

    return render(request, 'HUMANRESOURCE/employee/general/employee_update.html', {
        'company'               : Company.objects.first(),
        'employee'              : employee,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def employee_personal_create(request, id):
    try:
        employee    = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Employee ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form        = EmployeePersonalInfoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HUMANRESOURCE:employee_address_create', id=id)
    else:
        form        = EmployeePersonalInfoModelForm(initial={'employee': employee})
    
    return render(request, 'HUMANRESOURCE/employee/personal/employee_personal_create.html', {
        'company'               : Company.objects.first(),
        'employee'              : employee,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def employee_personal_update(request, id):
    try:
        personal    = EmployeePersonalInfo.objects.get(id=id)
    except EmployeePersonalInfo.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Employee Personal Info ID : {} does not exist.'.format(id)})
    
    if request.method == 'POST':
        form        = EmployeePersonalInfoModelForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('HUMANRESOURCE:employee_detail', id=form.cleaned_data['employee'].id)
    else:
        form        = EmployeePersonalInfoModelForm(instance=personal)

    return render(request, 'HUMANRESOURCE/employee/personal/employee_personal_update.html', {
        'company'               : Company.objects.first(),
        'personal'              : personal,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def employee_address_create(request, id):
    try:
        employee    = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Employee ID : {} does not exist.'.format(id)})

    if request.method == 'POST':
        form        = EmployeeAddressModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HUMANRESOURCE:employee_detail', id=id)
    else:
        form        = EmployeeAddressModelForm(initial={'employee': employee})
    
    return render(request, 'HUMANRESOURCE/employee/address/employee_address_create.html', {
        'company'               : Company.objects.first(),
        'employee'              : employee,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def employee_address_update(request, id):
    try:
        address    = EmployeeAddress.objects.get(id=id)
    except EmployeeAddress.DoesNotExist:
        return render(request, 'MAIN/page_not_found.html', {'message': 'Employee Address Info ID : {} does not exist.'.format(id)})
    
    if request.method == 'POST':
        form        = EmployeeAddressModelForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('HUMANRESOURCE:employee_detail', id=form.cleaned_data['employee'].id)
    else:
        form        = EmployeeAddressModelForm(instance=address)

    return render(request, 'HUMANRESOURCE/employee/address/employee_address_update.html', {
        'company'               : Company.objects.first(),
        'address'               : address,
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
