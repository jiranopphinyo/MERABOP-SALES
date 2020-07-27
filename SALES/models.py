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

#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def increment_customer_id():
    last_customer_id        = Customer.objects.order_by('id').last()
    if not last_customer_id:
        return '000001'
    else:
        new_customer_id     = str(int(last_customer_id.id) + 1).zfill(6)
        return new_customer_id

class Customer(models.Model):
    id                      = models.CharField("Customer ID", max_length=20, primary_key=True, default=increment_customer_id, editable=False, unique=True)
    name                    = models.CharField("Customer Name", max_length=200)
    description             = models.TextField("Description", null=True, blank=True)
    email                   = models.EmailField("Email", null=True, blank=True)
    phone                   = models.CharField("Phone Number", max_length=50, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "CUSTOMER | CUSTOMER GENERAL INFO"
        ordering            = ["id"]

    def __str__(self):
        return "{} - {}".format(self.id, self.name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerAddress(models.Model):
    id                      = models.AutoField("Customer Address ID", primary_key=True, editable=False, unique=True)
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
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
        verbose_name_plural = "CUSTOMER | CUSTOMER ADDRESS INFO"
        ordering            = ["customer__id"]
    
    def __str__(self):
        return "{} - {} | {}".format(self.customer.id, self.customer.name, self.address_name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerContactPerson(models.Model):
    id                      = models.AutoField("Customer Contact Person ID", primary_key=True, editable=False, unique=True)
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    fullname                = models.CharField("Fullname", max_length=100)
    job_title               = models.CharField("Job Title", max_length=100)
    phone                   = models.CharField("Phone Number", max_length=50, blank=True)
    email                   = models.EmailField("Email", null=True, blank=True)
    is_active               = models.BooleanField("Is Active?", default=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "CUSTOMER | CUSTOMER CONTACT PERSON INFO"
        ordering            = ["customer__id"]

    def __str__(self):
        return "{} - {} | {} ({})".format(self.customer.id, self.customer.name, self.fullname, self.job_title)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class CustomerPaymentTerm(models.Model):
    id                      = models.AutoField("Customer Payment Term ID", primary_key=True, editable=False, unique=True)
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    payment_term            = models.ForeignKey(PaymentTerm, on_delete=models.CASCADE, verbose_name="Payment Term")
    credit_day              = models.PositiveIntegerField("Credit Day", default=0)
    credit_amount           = models.DecimalField("Credit Amount", max_digits=20, decimal_places=2, default=0)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "CUSTOMER | CUSTOMER PAYMENT TERM INFO"
        ordering            = ["customer__id"]

    def __str__(self):
        return "{} - {} | {}".format(self.customer.id, self.customer.name, self.payment_term)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PersonInCharge(models.Model):
    id                      = models.AutoField("Person In Charge ID", primary_key=True, editable=False, unique=True)
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    sales_reps              = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Sales Reps")
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PERSON IN CHARGE | PERSON IN CHARGE"
    
    def __str__(self):
        return "{} - {} | SALES REPS: {}".format(self.customer.id, self.customer.name, self.sales_reps.first_name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def increment_purchase_requisition_id():
    last_purchase_requisition_id            = PurchaseRequisition.objects.order_by('id').last()
    if not last_purchase_requisition_id:
        return "PR" + str(datetime.date.today().year + 543)[2:] + '00001'
    else:
        purchase_requisition_id             = last_purchase_requisition_id.id
        purchase_requisition_year           = int("20" + str(int(purchase_requisition_id[2:4]) - int(43)))
        today_year                          = int(datetime.date.today().year)
        if purchase_requisition_year == today_year:
            purchase_requisition_int        = int(purchase_requisition_id[4:])
            new_purchase_requisition_int    = purchase_requisition_int + 1
            new_purchase_requisition_id     = "PR" + str(str(datetime.date.today().year + 543)[2:]) + str(new_purchase_requisition_int).zfill(5)
        else:
            new_purchase_requisition_id     = "PR" + str(str(datetime.date.today().year + 543)[2:]) + "00001"

    return new_purchase_requisition_id

class PurchaseRequisition(models.Model):
    id                      = models.CharField("Purchase Requisition ID", max_length=20, primary_key=True, default=increment_purchase_requisition_id, editable=False, unique=True)
    date                    = models.DateField("Purchase Requisition Date", default=timezone.localdate)
    estimate_needed_date    = models.DateField("Estimate Needed Date")
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PURCHASE REQUISITION | PURCHASE REQUISITION"
        ordering            = ["-id"]

    def __str__(self):
        return "{} | ESTIMATE NEEDED DATE: {}".format(self.id, self.estimate_needed_date)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionItem(models.Model):
    id                      = models.AutoField("Purchase Requisition Item ID", primary_key=True, editable=False, unique=True)
    purchase_requisition    = models.ForeignKey(PurchaseRequisition, on_delete=models.CASCADE, verbose_name="Purchase Requisition")
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity                = models.DecimalField("Quantity", max_digits=20, decimal_places=2, default=0.00)
    unit_price              = models.DecimalField("Unit Price", max_digits=20, decimal_places=2, default=0.00)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PURCHASE REQUISITION | PURCHASE REQUISITION ITEM"
        ordering            = ["-purchase_requisition__id"]

    def __str__(self):
        return "{} | {} - {}".format(self.purchase_requisition.id, self.product.id, self.product.name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionStatusLog(models.Model):
    id                      = models.AutoField("Purhase Requisition Status ID", primary_key=True, editable=False, unique=True)
    purchase_requisition    = models.ForeignKey(PurchaseRequisition, on_delete=models.CASCADE, verbose_name="Purchase Requisition")
    status                  = models.ForeignKey(PurchaseRequisitionStatus, on_delete=models.CASCADE, verbose_name="Purchase Requisition Status")
    user                    = models.CharField("User", max_length=50)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "PURCHASE REQUISITION | PURCHASE REQUISITION STATUS LOG"
        ordering            = ["-purchase_requisition__id"]

    def __str__(self):
        return "{} | STATUS: {}".format(self.purchase_requisition.id, self.status.purchase_requisition_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
ESTIMATE_DELIVERY_DAY = (
    ("1 - 3", "1 - 3"),
    ("1 - 5", "1 - 5"),
    ("1 - 7", "1 - 7"),
    ("1 - 10 ", "1 - 10 "),
    ("1 - 15 ", "1 - 15 "),
    ("1 - 30 ", "1 - 30 "),
)

def increment_quotation_id():
    last_quotation_id = Quotation.objects.all().order_by('id').last()
    if not last_quotation_id:
        return 'QT' + str(datetime.date.today().year + 543)[2:] + '00001'
    else:
        quotation_id            = last_quotation_id.id
        quotation_year          = int("20" + str(int(quotation_id[2:4]) - int(43)))
        today_year              = int(datetime.date.today().year)
        if quotation_year == today_year:
            quotation_int       = int(quotation_id[4:])
            new_quotation_int   = quotation_int + 1
            new_quotation_id    = "QT" + str(str(datetime.date.today().year + 543)[2:]) + str(new_quotation_int).zfill(5)
        else:
            new_quotation_id    = "QT" + str(str(datetime.date.today().year + 543)[2:]) + "00001"

    return new_quotation_id

class Quotation(models.Model):
    id                      = models.CharField("Quotation ID", max_length=20, primary_key=True, default=increment_quotation_id, editable=False, unique=True)
    date                    = models.DateField("Quotation Date", default=timezone.localdate)
    valid_until             = models.DateField("Valid Until")
    estimate_delivery_day   = models.CharField("Estimate Delivery Day", max_length=20, choices=ESTIMATE_DELIVERY_DAY)
    sales_reps              = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Sales Reps")
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    customer_billing_address= models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, verbose_name="Customer Billing Address")
    customer_contact_person = models.ForeignKey(CustomerContactPerson, on_delete=models.CASCADE, verbose_name="Customer Contact Person")
    payment_term            = models.CharField("Payment Term", max_length=20, choices=(("CREDIT", "CREDIT"), ("CASH", "CASH")))
    sub_total               = models.DecimalField("Sub Total", max_digits=20, decimal_places=2, default=0.00, editable=False)
    discount                = models.DecimalField("Discount", max_digits=20, decimal_places=2, default=0.00)
    after_discount          = models.DecimalField("After Discount", max_digits=20, decimal_places=2, default=0.00, editable=False)
    vat                     = models.DecimalField("Value Added Tax", max_digits=20, decimal_places=2, default=0.00, editable=False)
    net_total               = models.DecimalField("Net Total", max_digits=20, decimal_places=2, default=0.00, editable=False)
    baht_text               = models.CharField("Baht Text", max_length=200, default="", editable=False)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "QUOTATION | QUOTATION"
        ordering            = ["-id"]
    
    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        quotation_items     = self.quotation_items.all()
        sub_total           = quotation_items.aggregate(Sum('amount'))['amount__sum'] if quotation_items.exists() else 0.00
        self.sub_total      = Decimal(sub_total)
        self.after_discount = Decimal(sub_total) - Decimal(self.discount)
        self.vat            = Decimal(self.after_discount) * Decimal(0.07)
        self.net_total      = Decimal(self.after_discount) + Decimal(self.vat)
        self.baht_text      = bahttext(self.net_total)
        super().save(*args, **kwargs)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationItem(models.Model):
    id                      = models.AutoField("Quotation Item ID", primary_key=True, editable=False, unique=True)
    quotation               = models.ForeignKey(Quotation, on_delete=models.CASCADE, verbose_name="Quotation", related_name="quotation_items")
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity                = models.DecimalField("Quantity", max_digits=20, decimal_places=2, default=0.00)
    unit_price              = models.DecimalField("Unit Price", max_digits=20, decimal_places=2, default=0.00)
    amount                  = models.DecimalField("Amount", max_digits=20, decimal_places=2, default=0.00, editable=False)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "QUOTATION | QUOTATION ITEM"
        ordering            = ["-quotation__id"]

    def __str__(self):
        return "{} | {} - {}".format(self.quotation.id, self.product.id, self.product.name)
    
    def save(self, *args, **kwargs):
        self.amount         = Decimal(self.quantity) * Decimal(self.unit_price)
        super().save(*args, **kwargs)
        self.quotation.save()
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationStatusLog(models.Model):
    id                      = models.AutoField("Quotation Status Log ID", primary_key=True, editable=False, unique=True)
    quotation               = models.ForeignKey(Quotation, on_delete=models.CASCADE, verbose_name="Quotation")
    status                  = models.ForeignKey(QuotationStatus, on_delete=models.CASCADE, verbose_name="Quotation Status")
    user                    = models.CharField("User", max_length=50)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "QUOTATION | QUOTATION STATUS LOG"
        ordering            = ["-quotation__id"]

    def __str__(self):
        return "{} | STATUS: {}".format(self.quotation.id, self.status.quotation_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
def increment_sales_order_id():
    last_sales_order_id     = SalesOrder.objects.order_by('id').last()
    if not last_sales_order_id:
        return 'SO' + str(datetime.date.today().year + 543)[2:] + '00001'
    else:
        sales_order_id      = last_sales_order_id.id
        sales_order_year    = int("20" + str(int(sales_order_id[2:4]) - int(43)))
        today_year          = int(datetime.date.today().year)
        if sales_order_year == today_year:
            sales_order_int = int(sales_order_id[4:])
            new_sales_order_int   = sales_order_int + 1
            new_sales_order_id    = "QT" + str(str(datetime.date.today().year + 543)[2:]) + str(new_sales_order_int).zfill(5)
        else:
            new_sales_order_id    = "QT" + str(str(datetime.date.today().year + 543)[2:]) + "00001"

    return new_sales_order_id

class SalesOrder(models.Model):
    id                      = models.CharField("Sales Order ID", max_length=20, primary_key=True, default=increment_sales_order_id, editable=False, unique=True)
    date                    = models.DateField("Sales Order Date", default=timezone.localdate)
    delivery_date           = models.DateField("Delivery Date")
    sales_reps              = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Sales Reps")
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    customer_billing_address= models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, verbose_name="Customer Billing Address", related_name="customer_billing_address")
    customer_delivery_address=models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, verbose_name="Customer Delivery Address", related_name="customer_delivery_address")
    customer_payment_term   = models.ForeignKey(CustomerPaymentTerm, on_delete=models.CASCADE, verbose_name="Customer Payment Term")
    sub_total               = models.DecimalField("Sub Total", max_digits=20, decimal_places=2, default=0.00, editable=False)
    vat                     = models.DecimalField("Value Added Tax", max_digits=20, decimal_places=2, default=0.00, editable=False)
    net_total               = models.DecimalField("Net Total", max_digits=20, decimal_places=2, default=0.00, editable=False)
    baht_text               = models.CharField("Baht Text", max_length=200, default="", editable=False)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "SALES ORDER | SALES ORDER"
        ordering            = ["-id"]

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        sales_order_items   = self.sales_order_items.all()
        sub_total           = sales_order_items.aggregate(Sum('amount'))['amount__sum'] if sales_order_items.exists() else 0.00
        self.sub_total      = Decimal(sub_total)
        self.vat            = Decimal(self.sub_total) * Decimal(0.07)
        self.net_total      = Decimal(self.sub_total) + Decimal(self.vat)
        self.baht_text      = Decimal(self.net_total)
        super().save(*args, **kwargs)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderItem(models.Model):
    id                      = models.AutoField("Sales Order Item ID", primary_key=True, editable=False, unique=True)
    sales_order             = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, verbose_name="Sales Order", related_name="sales_order_items")
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity                = models.DecimalField("Quantity", max_digits=20, decimal_places=2, default=0.00)
    unit_price              = models.DecimalField("Unit Price", max_digits=20, decimal_places=2, default=0.00)
    amount                  = models.DecimalField("Amount", max_digits=20, decimal_places=2, default=0.00, editable=False)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "SALES ORDER | SALES ORDER ITEM"
        ordering            = ["-sales_order__id"]

    def __str__(self):
        return "{} | {} - {}".format(self.sales_order.id, self.product.id, self.product.name)

    def save(self, *args, **kwargs):
        self.amount         = Decimal(self.quantity) * Decimal(self.unit_price)
        super().save(*args, **kwargs)
        self.sales_order.save()
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderStatusLog(models.Model):
    id                      = models.AutoField("Sales Order Status Log ID", primary_key=True, editable=False, unique=True)
    sales_order             = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, verbose_name="Sales Order")
    status                  = models.ForeignKey(SalesOrderStatus, on_delete=models.CASCADE, verbose_name="Sales Order Status")
    user                    = models.CharField("User", max_length=50)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "SALES ORDER | SALES ORDER STATUS LOG"
        ordering            = ["-sales_order__id"]

    def __str__(self):
        return "{} | STATUS: {}".format(self.sales_order.id, self.status.sales_order_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReport(models.Model):
    id                      = models.AutoField("Daily Report ID", primary_key=True, editable=False, unique=True)
    date                    = models.DateField("Daily Report Date", default=timezone.localdate)
    sales_reps              = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Sales Reps")
    contact_method          = models.ForeignKey(DailyReportContactMethod, on_delete=models.CASCADE, verbose_name="Contact Method")
    customer                = models.ForeignKey(PersonInCharge, on_delete=models.CASCADE, verbose_name="Customer")
    customer_contact_person = models.ForeignKey(CustomerContactPerson, on_delete=models.CASCADE, verbose_name="Contact Person")
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "DAILY REPORT | DAILY REPORT"
        ordering            = ["-date"]

    def __str__(self):
        return "DAILY REPORT OF: {} | {} ON {}".format(self.sales_reps.first_name, self.customer.customer.name, self.date)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportItem(models.Model):
    id                      = models.AutoField("Daily Report Item ID", primary_key=True, editable=False, unique=True)
    daily_report            = models.ForeignKey(DailyReport, on_delete=models.CASCADE, verbose_name="Daily Report")
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    daily_report_type       = models.ForeignKey(DailyReportType, on_delete=models.CASCADE, verbose_name="Daily Report Type")
    quantity                = models.DecimalField("Quantity", max_digits=20, decimal_places=2, default=0.00, null=True, blank=True)
    unit_price              = models.DecimalField("Unit Price", max_digits=20, decimal_places=2, default=0.00, null=True, blank=True)
    is_accept               = models.NullBooleanField("Is Accept", null=True, blank=True)
    remark                  = models.TextField("Remark", null=True, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "DAILY REPORT | DAILY REPORT ITEM"
        ordering            = ['-daily_report__id']

    def __str__(self):
        return "{} - {}".format(self.daily_report, self.id)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
