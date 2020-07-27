from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.contrib.auth.decorators import login_required

### SETTINGS:: ALL
from SETTINGS.decorators import *
### SALES:: ALL
from SALES.models import *
from SALES.forms import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allowed_users(allowed_departments=[])
def person_in_charge_list(request):
    person_in_charges   = PersonInCharge.objects.order_by('-id')[:10]

    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        if search_text:
            person_in_charges   = PersonInCharge.objects.filter(
                Q(customer__id__iexact              = search_text) |
                Q(customer__name__icontains         = search_text) |
                Q(sales_reps__first_name__iexact    = search_text)
            )
        else:
            person_in_charges   = None
    
    return render(request, 'SALES/person_in_charge/person_in_charge_list.html', {
        'company'           : Company.objects.first(),
        'person_in_charges' : person_in_charges,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@login_required
# @allow_users(allowed_departments=[])
def person_in_charge_create(request):
    form        = PersonInChargeModelForm()
    if request.method == 'POST':
        form    = PersonInChargeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SALES:person_in_charge_list')

    return render(request, 'SALES/person_in_charge/person_in_charge_create.html', {
        'company'               : Company.objects.first(),
        'form'                  : form,
    })
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
