from django.db import models
from django.db.models import Sum, Avg, Count, Max, Min
from decimal import Decimal
from bahttext import bahttext
from django.utils import timezone
import datetime

### SETTINGS:: ALL
from SETTINGS.models import *
### HUMANRESOURCE:: ALL
from HUMANRESOURCE.models import *
### PURCHASE:: ALL
from PURCHASE.models import *
### SALES:: ALL
from SALES.models import *

#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def increment_lot_number_id():
    last_lot_number_id  = ProductLotNumber.objects.order_by('id').last()
    if not last_lot_number_id:
        return "MRB" + str(datetime.date.today()) + "01" #MRB2020072001
    else:
        lot_number_id           = last_lot_number_id.id
        lot_number_date         = lot_number_id[3:11]
        today_date              = str(datetime.date.today())
        if lot_number_date == today_date:
            lot_number_int      = int(lot_number_id[11:])
            new_lot_number_int  = lot_number_int + 1
            new_lot_number_id   = "MRB" + str(datetime.date.today()) + str(new_lot_number_int).zfill(2)
        else:
            new_lot_number_id   = "MRB" + str(datetime.date.today()) + "01"
    return new_lot_number_id

class ProductLotNumber(models.Model):
    id                      = models.CharField("Product Lot No.", max_length=20, primary_key=True, default=increment_lot_number_id, editable=False, unique=True)
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    original_lot_number     = models.CharField("Original Lot No.", max_length=50, null=True, blank=True)
    received_date           = models.DateField("Received Date", default=timezone.localdate)
    receiving_amount        = models.DecimalField("Receiving Amount", max_digits=20, decimal_places=2, default=0.00)
    remaining_amount        = models.DecimalField("Remaining Amount", max_digits=20, decimal_places=2, default=0.00)
    manufactured_date       = models.DateField("Manufactured Date")
    expired_date            = models.DateField("Expired Date")
    unit_cost               = models.DecimalField("Unit Cost", max_digits=20, decimal_places=2, default=0.00)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PRODUCT | PRODUCT LOT NUMBER"
        ordering            = ["-id"]

    def __str__(self):
        return "{} | {} | RECEIVED: {} | MFG: {} | EXP: {}".format(self.id, self.product.name, str(self.received_date), str(self.manufactured_date), str(self.expired_date))