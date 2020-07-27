from django.db import models


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Company(models.Model):
    company_name            = models.CharField("Company Name", max_length=200)
    brand_name              = models.CharField("Brand Name", max_length=50)
    address_line_1          = models.CharField("Address Line 1", max_length=50)
    address_line_2          = models.CharField("Address Line 2", max_length=50, blank=True)
    sub_district            = models.CharField("Sub District / Tumbol", max_length=50)
    district                = models.CharField("District", max_length=50)
    province                = models.CharField("Province", max_length=50)
    postal_code             = models.CharField("ZIP / Postal Code", max_length=10)
    country                 = models.CharField("Country", max_length=100)
    phone                   = models.CharField("Phone Number", max_length=20)
    fax                     = models.CharField("Fax Number", max_length=20)
    email                   = models.EmailField("Email")
    # favicons
    # logo

    class Meta:
        verbose_name_plural = "COMPANY | COMPANY SETTINGS"
        ordering            = ["company_name"]

    def __str__(self):
        return "{} | {}".format(self.company_name, self.brand_name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SupplierType(models.Model):
    id                      = models.AutoField("Supplier Type ID", primary_key=True, editable=False, unique=True)
    supplier_type           = models.CharField("Supplier Type", max_length=100)

    class Meta:
        verbose_name_plural = "SUPPLIER | SUPPLIER TYPE"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.supplier_type)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Country(models.Model):
    id                      = models.AutoField("Country ID", primary_key=True, editable=False, unique=True)
    name                    = models.CharField("Country Name", max_length=200)

    class Meta:
        verbose_name_plural = "COUNTRY | COUNTRY LIST"
        ordering            = ["name"]

    def __str__(self):
        return "{}".format(self.name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PaymentTerm(models.Model):
    id                      = models.AutoField("Payment Term ID", primary_key=True, editable=False, unique=True)
    payment_term            = models.CharField("Payment Term", max_length=100)

    class Meta:
        verbose_name_plural = "PAYMENT TERM | PAYMENT TERM"
        ordering            = ["payment_term"]

    def __str__(self):
        return "{}".format(self.payment_term)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PackingType(models.Model):
    id                      = models.AutoField("Packing Type ID", primary_key=True, editable=False, unique=True)
    packing_type            = models.CharField("Packing Type", max_length=20)

    class Meta:
        verbose_name_plural = "PRODUCT | PACKING TYPE"
        ordering            = ["packing_type"]

    def __str__(self):
        return "{}".format(self.packing_type)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PackingMaterial(models.Model):
    id                      = models.AutoField("Packing Material ID", primary_key=True, editable=False, unique=True)
    packing_material        = models.CharField("Packing Material", max_length=20)

    class Meta:
        verbose_name_plural = "PRODUCT | PACKING MATERIAL"
        ordering            = ["packing_material"]

    def __str__(self):
        return "{}".format(self.packing_material)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseRequisitionStatus(models.Model):
    id                      = models.AutoField("Purchase Requisition Status ID", primary_key=True, editable=False, unique=True)
    purchase_requisition_status = models.CharField("Purchase Requisition Status", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | PURCHASE REQUISITION | PURCHASE REQUISITION STATUS"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.purchase_requisition_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class QuotationStatus(models.Model):
    id                      = models.AutoField("Quotation Status ID", primary_key=True, editable=False, unique=True)
    quotation_status        = models.CharField("Quotation Status", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | QUOTATION | QUOTATION STATUS"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.quotation_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class SalesOrderStatus(models.Model):
    id                      = models.AutoField("Sales Order Status ID", primary_key=True, editable=False, unique=True)
    sales_order_status      = models.CharField("Sales Order Status", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | SALES ORDER | SALES ORDER STATUS"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.sales_order_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class PurchaseOrderStatus(models.Model):
    id                      = models.AutoField("Purchase Order Status ID", primary_key=True, editable=False, unique=True)
    purchase_order_status   = models.CharField("Purchase Order Status", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | PURCHASE ORDER | PURCHASE ORDER STATUS"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.purchase_order_status)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportContactMethod(models.Model):
    id                      = models.AutoField("Daily Report Contact Method ID", primary_key=True, editable=False, unique=True)
    daily_report_contact_method = models.CharField("Daily Report Contact Method", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | DAILY REPORT | DAILY REPORT CONTACT METHOD"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.daily_report_contact_method)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class DailyReportType(models.Model):
    id                      = models.AutoField("Daily Report Type ID", primary_key=True, editable=False, unique=True)
    daily_report_type       = models.CharField("Daily Report Type", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | DAILY REPORT | DAILY REPORT TYPE"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.daily_report_type)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class LivingArrangement(models.Model):
    id                      = models.AutoField("Living Arrangement ID", primary_key=True, editable=False, unique=True)
    living_arrangement      = models.CharField("Living Arrangement", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | EMPLOYEE | LIVING ARRANGEMENT"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.living_arrangement)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Race(models.Model):
    id                      = models.AutoField("Race ID", primary_key=True, editable=False, unique=True)
    race                    = models.CharField("Race", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | EMPLOYEE | RACE"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.race)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Nationality(models.Model):
    id                      = models.AutoField("Nationality ID", primary_key=True, editable=False, unique=True)
    nationality             = models.CharField("Nationality", max_length=20)

    class Meta:
        verbose_name_plural = "SETTINGS | EMPLOYEE | NATIONALITY"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.nationality)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Division(models.Model):
    id                      = models.AutoField("Division ID", primary_key=True, editable=False, unique=True)
    division                = models.CharField("Division", max_length=100)
    
    class Meta:
        verbose_name_plural = "SETTINGS | ORGANIZATION | DIVISION"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.division)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Department(models.Model):
    id                      = models.AutoField("Department ID", primary_key=True, editable=False, unique=True)
    division                = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Division")
    department              = models.CharField("Department", max_length=100)
    
    class Meta:
        verbose_name_plural = "SETTINGS | ORGANIZATION | DEPARTMENT"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.department)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Section(models.Model):
    id                      = models.AutoField("Section ID", primary_key=True, editable=False, unique=True)
    department              = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Department")
    section                 = models.CharField("Section", max_length=100)
    
    class Meta:
        verbose_name_plural = "SETTINGS | ORGANIZATION | SECTION"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.section)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Position(models.Model):
    id                      = models.AutoField("Position ID", primary_key=True, editable=False, unique=True)
    position                = models.CharField("Position", max_length=100)

    class Meta:
        verbose_name_plural = "SETTINGS | ORGANIZATION | POSITION"
        ordering            = ["id"]

    def __str__(self):
        return "{}".format(self.position)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
