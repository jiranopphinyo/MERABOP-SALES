from django.db import models
from django.db.models import Sum, Avg, Count, Max, Min
from decimal import Decimal
from bahttext import bahttext
from django.utils import timezone
import datetime

# SETTINGS:: ALL
from SETTINGS.models import *

#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def increment_supplier_id():
    last_supplier_id        = Supplier.objects.order_by('id').last()
    if not last_supplier_id:
        return '000001'
    else:
        new_supplier_id     = str(int(last_supplier_id.id) + 1).zfill(6)
        return new_supplier_id

class Supplier(models.Model):
    id                      = models.CharField("Supplier ID", max_length=20, primary_key=True, default=increment_supplier_id, editable=False, unique=True)
    name                    = models.CharField("Supplier Name", max_length=200)
    supplier_type           = models.ForeignKey(SupplierType, on_delete=models.CASCADE, verbose_name="Supplier Type")
    description             = models.TextField("Description", null=True, blank=True)
    email                   = models.EmailField("Email", null=True, blank=True)
    website                 = models.URLField("Website", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "SUPPLIER | SUPPLIER GENERAL INFO"
        ordering            = ["id"]

    def __str__(self):
        return "{} - {}".format(self.id, self.name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierAddress(models.Model):
    id                      = models.AutoField("Supplier Address ID", primary_key=True, editable=False, unique=True)
    supplier                = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Supplier")
    address_name            = models.CharField("Address Name", max_length=100)
    address_line_1          = models.CharField("Address Line 1", max_length=100)
    address_line_2          = models.CharField("Address Line 2", max_length=100, null=True, blank=True)
    sub_district            = models.CharField("Sub District", max_length=100)
    district                = models.CharField("District", max_length=100)
    province                = models.CharField("Province", max_length=100)
    postal_code             = models.CharField("ZIP/Postal Code", max_length=10)
    country                 = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country")
    phone                   = models.CharField("Phone Number", max_length=50, blank=True)
    fax                     = models.CharField("Fax Number", max_length=50, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "SUPPLIER | SUPPLIER ADDRESS INFO"
        ordering            = ["supplier__id"]
    
    def __str__(self):
        return "{} - {} | {}".format(self.supplier.id, self.supplier.name, self.address_name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierContactPerson(models.Model):
    id                      = models.AutoField("Supplier Contact Person ID", primary_key=True, editable=False, unique=True)
    supplier                = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Supplier")
    fullname                = models.CharField("Fullname", max_length=100)
    job_title               = models.CharField("Job Title", max_length=100)
    phone                   = models.CharField("Phone Number", max_length=50, blank=True)
    email                   = models.EmailField("Email", null=True, blank=True)
    is_active               = models.BooleanField("Is Active?", default=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "SUPPLIER | SUPPLIER CONTACT PERSON INFO"
        ordering            = ["supplier__id"]

    def __str__(self):
        return "{} - {} | {} ({})".format(self.supplier.id, self.supplier.name, self.fullname, self.job_title)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierPaymentTerm(models.Model):
    id                      = models.AutoField("Supplier Payment Term ID", primary_key=True, editable=False, unique=True)
    supplier                = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Supplier")
    payment_term            = models.ForeignKey(PaymentTerm, on_delete=models.CASCADE, verbose_name="Payment Term")
    credit_day              = models.PositiveIntegerField("Credit Day", default=0)
    credit_amount           = models.DecimalField("Credit Amount", max_digits=20, decimal_places=2, default=0)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "SUPPLIER | SUPPLIER PAYMENT TERM INFO"
        ordering            = ["supplier__id"]

    def __str__(self):
        return "{} - {} | {}".format(self.supplier.id, self.supplier.name, self.payment_term)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Product(models.Model):
    id                      = models.CharField("Product ID", max_length=20, primary_key=True, unique=True)
    name                    = models.CharField("Product Name", max_length=200)
    net_weight              = models.DecimalField("Net Weight", max_digits=20, decimal_places=2, default=0.00)
    gross_weight            = models.DecimalField("Gross Weight", max_digits=20, decimal_places=2, default=0.00)
    weighing_unit           = models.CharField("Weighing Unit", max_length=20, default="KG")
    packing_type            = models.ForeignKey(PackingType, on_delete=models.CASCADE, verbose_name="Packing Type")
    packing_material        = models.ForeignKey(PackingMaterial, on_delete=models.CASCADE, verbose_name="Packing Material")
    cbm                     = models.DecimalField("Cubic Metre", max_digits=20, decimal_places=2, default=0.00)
    characteristic          = models.TextField(blank=True)
    shipped_country         = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Shipped Country", related_name="shipped_country")
    manufactured_country    = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Manufactured Country", related_name="manufactured_country")
    supplier                = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Supplier")
    total_remaining_amount  = models.DecimalField("Total Remaining Amount", max_digits=20, decimal_places=2, default=0.00, editable=False)
    suggested_sales_price   = models.DecimalField("Suggested Sales Price", max_digits=20, decimal_places=2, default=0.00, editable=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PRODUCT | PRODUCT GENERAL INFO"
        ordering            = ["id"]

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def get_product_packing(self):
        return "{} {}/{}".format(self.net_weight, self.weighing_unit, self.packing_type)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def increment_purchase_order_id():
    last_purchase_order_id  = PurchaseOrder.objects.order_by('id').last()
    if not last_purchase_order_id:
        return 'PO' + str(datetime.date.today().year + 543)[2:] + '00001'
    else:
        purchase_order_id   = last_purchase_order_id.id
        purchase_order_year = int("20" + str(int(purchase_order_id[2:4]) -int(43)))
        today_year          = int(datetime.date.today().year)
        if purchase_order_year == today_year:
            purchase_order_int      = int(purchase_order_id[4:])
            new_purchase_order_int  = purchase_order_int + 1
            new_purchase_order_id   = "PO" + str(str(datetime.date.today().year + 543)[2:]) + str(new_purchase_order_int).zfill(5)
        else:
            new_purchase_order_id   = "PO" + str(str(datetime.date.today().year + 543)[2:]) + "00001"
        
    return new_purchase_order_id

class PurchaseOrder(models.Model):
    id                      = models.CharField("Purchase Order ID", max_length=20, primary_key=True, default=increment_purchase_order_id, editable=False, unique=True)
    date                    = models.DateField("Purchase Order Date", default=timezone.localdate)
    # purchase_requisition
    # currency ($, ฿)
    supplier                = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Supplier")
    supplier_billing_address= models.ForeignKey(SupplierAddress, on_delete=models.CASCADE, verbose_name="Supplier Billing Address")
    supplier_contact_person = models.ForeignKey(SupplierContactPerson, on_delete=models.CASCADE, verbose_name="Supplier Contact Person")
    supplier_payment_term   = models.ForeignKey(SupplierPaymentTerm, on_delete=models.CASCADE, verbose_name="Supplier Payment Term")
    sub_total               = models.DecimalField("Sub Total", max_digits=20, decimal_places=2, default=0.00, editable=False)
    vat                     = models.DecimalField("Value Added Tax", max_digits=20, decimal_places=2, default=0.00, editable=False)
    net_total               = models.DecimalField("Net Total", max_digits=20, decimal_places=2, default=0.00, editable=False)
    baht_text               = models.CharField("Baht Text", max_length=200, default="", editable=False)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PURCHASE ORDER | PURCHASE ORDER"
        ordering            = ["-id"]

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        purchase_order_items= self.purchase_order_items.all()
        sub_total           = purchase_order_items.aggregate(Sum('amount'))['amount__sum'] if purchase_order_items.exists() else 0.00
        self.sub_total      = Decimal(sub_total)
        self.vat            = Decimal(self.sub_total) * Decimal(0.07)
        self.net_total      = Decimal(self.sub_total) + Decimal(self.vat)
        self.baht_text      = Decimal(self.net_total)
        super().save(*args, **kwargs)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderItem(models.Model):
    id                      = models.AutoField("Purchase Order Item ID", primary_key=True, editable=False, unique=True)
    purchase_order          = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, verbose_name="Purchase Order", related_name="purchase_order_items")
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity                = models.DecimalField("Quantity", max_digits=20, decimal_places=2, default=0.00)
    unit_price              = models.DecimalField("Unit Price", max_digits=20, decimal_places=2, default=0.00)
    amount                  = models.DecimalField("Amount", max_digits=20, decimal_places=2, default=0.00, editable=False)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PURCHASE ORDER | PURCHASE ORDER ITEM"
        ordering            = ["-purchase_order__id"]

    def __str__(self):
        return "{} | {} - {}".format(self.purchase_order.id, self.product.id, self.product.name)

    def save(self, *args, **kwargs):
        self.amount         = Decimal(self.quantity) * Decimal(self.unit_price)
        super().save(*args, **kwargs)
        self.purchase_order.save()
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderStatusLog(models.Model):
    id                      = models.AutoField("Purchase Order Status Log ID", primary_key=True, editable=False, unique=True)
    purchase_order          = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, verbose_name="Purchase Order")
    status                  = models.ForeignKey(PurchaseOrderStatus, on_delete=models.CASCADE, verbose_name="Purchase Order Status")
    user                    = models.CharField("User", max_length=50)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PURCHASE ORDER | PURCHASE ORDER STATUS LOG"
        ordering            = ["-purchase_order__id"]

    def __str__(self):
        return "{} | STATUS: {}".format(self.purchase_order.id, self.status.purchase_order_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
