from common.mixins import BaseModel
from django.db import models


class GenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"


class PaymentMethodChoices(models.TextChoices):
    CASH = "C", "Cash"
    EFT = "E", "EFT"
    CHEQUE = "Q", "Cheque"


class Employee(BaseModel):
    title = models.CharField(max_length=200, blank=True)
    initials = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    other_names = models.CharField(max_length=200, blank=True)
    dob = models.DateField(null=True, blank=True)
    rsa_id_number = models.CharField(max_length=13, blank=True)
    passport_number = models.CharField(max_length=20, blank=True)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, related_name="employees")  # noqa: E501
    employee_code = models.CharField(max_length=200, blank=True)
    employment_date = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GenderChoices, null=True, blank=True)
    cell_no = models.CharField(max_length=20, blank=True)
    work_no = models.CharField(max_length=20, blank=True)
    payment_method = models.CharField(choices=PaymentMethodChoices, max_length=2, blank=True)  # noqa: E501
    pays_paye = models.BooleanField(null=True, blank=True)
    pays_uif = models.BooleanField(null=True, blank=True)
    basic_salary = models.DecimalField(max_digits=21, decimal_places=4, null=True, blank=True)  # noqa: E501
    job_title = models.CharField(max_length=200, blank=True)
