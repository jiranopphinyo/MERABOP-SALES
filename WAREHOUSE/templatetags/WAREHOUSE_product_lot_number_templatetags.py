from django import template
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum, Avg, Min, Max, Count

### SETTINGS:: ALL
from SETTINGS.models import *
### PURCHASE:: ALL
from PURCHASE.models import *
### WAREHOUSE:: ALL
from WAREHOUSE.models import *

register = template.Library()
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@register.simple_tag
def get_remaining_shelf_life_day(id):
    try:
        product_lot_number          = ProductLotNumber.objects.get(id=id)
    except:
        product_lot_number          = None
    
    if product_lot_number is not None:
        now                         = timezone.localdate()
        expired_date                = product_lot_number.expired_date
        remaining_shelf_life_day    = (expired_date - now).days
    else:
        remaining_shelf_life_day    = "-"

    return remaining_shelf_life_day
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
@register.simple_tag
def get_remaining_shelf_life_percent(id):
    try:
        product_lot_number          = ProductLotNumber.objects.get(id=id)
    except:
        product_lot_number          = None
    
    if product_lot_number is not None:
        now                         = timezone.localdate()
        expired_date                = product_lot_number.expired_date
        manufactured_date           = product_lot_number.manufactured_date
        remaining_shelf_life_percent= round((((expired_date - now).days) / ((expired_date - manufactured_date).days) * 100), 2)
    else:
        remaining_shelf_life_percent= "-"

    print(remaining_shelf_life_percent)
    
    return remaining_shelf_life_percent
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
