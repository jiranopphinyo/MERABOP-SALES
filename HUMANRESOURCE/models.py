from django.db import models
from django.contrib.auth.models import User

### SETTINGS:: ALL
from SETTINGS.models import *


#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
class Employee(models.Model):
    id                      = models.AutoField("Employee ID", primary_key=True, editable=False, unique=True)
    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name              = models.CharField("First Name", max_length=100, blank=True)
    last_name               = models.CharField("Last Name", max_length=100, blank=True)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "EMPLOYEE | EMPLOYEE GENERAL INFO"
        ordering            = ["first_name", "last_name"]

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
RELIGION = [
    ("African Traditional Religion", "African Traditional Religion"),
    ("Bahai", "Bahai"),
    ("Buddhism", "Buddhism"),
    ("Cao Dai", "Cao Dai"),
    ("Chinese Traditional Religion", "Chinese Traditional Religion"),
    ("Christainity", "Christianity"),
    ("Ethnic Religion", "Ethnic Religion"),
    ("Hinduism", "Hinduism"),
    ("Islam", "Islam"),
    ("Jainism", "Jainism"),
    ("Judaism", "Judaism"),
    ("Neo-Paganism", "Neo-Paganism"),
    ("Non - Religious", "Non - Religious"),
    ("Rastafari", "Rastafari"),
    ("Shinto", "Shinto"),
    ("Sikhism", "Sikhism"),
    ("Spiritsm", "Spiritsm"),
    ("Tenrikyo", "Tenrikyo"),
    ("Unitarian Universalism", "Unitarium Universalism"),
    ("Zoroastianism", "Zoroastianism"),
]

BLOOD_GROUP = [
    ("Blood Group O", "Blood Group O"),
    ("Blood Group A", "Blood Group A"),
    ("Blood Group B", "Blood Group B"),
    ("Blood Group AB", "Blood Group AB"),
]

MILITARY_STATUS = [
    ("Not yet served", "Not yet served"),
    ("Served", "Served"),
    ("Exempted", "Exempted"),
]

MARITAL_STATUS = [
    ("Single", "Single"),
    ("Married", "Married"),
    ("Separated", "Separated"),
    ("Divorced", "Divorced"),
    ("Widowed", "Widowed"),
]

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]

class EmployeePersonalInfo(models.Model):
    id                      = models.AutoField("Employee Personal Info ID", primary_key=True, editable=False, unique=True)
    employee                = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name="Employee")
    living_arrangement      = models.ForeignKey(LivingArrangement, on_delete=models.CASCADE, verbose_name="Living Arrangement")
    race                    = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Race")
    nationality             = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name="Nationality")
    religion                = models.CharField("Religion", max_length=50, choices=RELIGION)
    blood_group             = models.CharField("Blood Group", max_length=50, choices=BLOOD_GROUP)
    height                  = models.DecimalField("Height (cm.)", max_digits=5, decimal_places=2, default=0.00)
    weight                  = models.DecimalField("Weight (cm.)", max_digits=5, decimal_places=2, default=0.00)
    military_status         = models.CharField("Military Status", max_length=50, choices=MILITARY_STATUS)
    marital_status          = models.CharField("Marital Status", max_length=50, choices=MARITAL_STATUS)
    gender                  = models.CharField("Gender", max_length=50, choices=GENDER)
    birth_date              = models.DateField("Birth Date")
    email                   = models.EmailField("Email")
    phone                   = models.CharField("Phone Number", max_length=50)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "EMPLOYEE | EMPLOYEE PERSONAL INFO"
        ordering            = ["employee__first_name", "employee__last_name"]

    def __str__(self):
        return "{} {} | PERSONAL INFO".format(self.employee.first_name, self.employee.last_name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
ADDRESS_TYPE = [
    ("ที่อยู่ปัจจุบัน", "ที่อยู่ปัจจุบัน"),
    ("ที่อยู่ตามทะเบียนบ้าน", "ที่อยู่ตามทะเบียนบ้าน"),
    ("ที่อยู่อื่นๆ", "ที่อยู่อื่นๆ")
]

class EmployeeAddress(models.Model):
    id                      = models.AutoField("Employee Address ID", primary_key=True, editable=False, unique=True)
    employee                = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name="Employee")
    address_type            = models.CharField("Address Type", max_length=100, choices=ADDRESS_TYPE)
    address_line_1          = models.CharField("Address Line 1", max_length=50)
    address_line_2          = models.CharField("Address Line 2", max_length=50, blank=True)
    sub_district            = models.CharField("Sub District / Tumbol", max_length=50)
    district                = models.CharField("District", max_length=50)
    province                = models.CharField("Province", max_length=50) # ForeignKey to Province
    postal_code             = models.CharField("ZIP / Postal Code", max_length=10)
    country                 = models.CharField("Country", max_length=100) # ForeignKey to Country
    phone                   = models.CharField("Phone Number", max_length=20)
    created_at              = models.DateTimeField("Created at", auto_now_add=True)
    updated_at              = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name_plural = "EMPLOYEE | EMPLOYEE ADDRESS INFO"
        ordering            = ["employee__first_name", "employee__last_name"]

    def __str__(self):
        return "{} | ADDRESS INFO".format(self.employee.get_full_name)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
# class EmployeeFamily(models.Model):
#     id                      = models.AutoField("Employee Family ID", primary_key=True, editable=False, unique=True)
#     employee                = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name="Employee")
#     fullname                = models.CharField("Fullname", max_length=50)
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
# class EmployeeEducation(models.Model):
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
# class EmployeeSkill(models.Model):
#========================================================================================================================================================================================================================================================#
#========================================================================================================================================================================================================================================================#
# class EmployeeLicense(models.Model):