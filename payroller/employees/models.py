# ruff: noqa: DJ001, E501

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
    title = models.CharField(max_length=200, null=True, blank=True)
    initials = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    other_names = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    rsa_id_number = models.CharField(max_length=13, null=True, blank=True)
    passport_number = models.CharField(max_length=20, null=True, blank=True)
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, related_name="employees")
    employee_code = models.CharField(max_length=200, null=True, blank=True)
    employment_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GenderChoices, max_length=1, null=True, blank=True)
    cell_no = models.CharField(max_length=20, null=True, blank=True)
    work_no = models.CharField(max_length=20, null=True, blank=True)
    payment_method = models.CharField(choices=PaymentMethodChoices, max_length=2, null=True, blank=True)
    pays_paye = models.BooleanField(null=True, blank=True)
    pays_uif = models.BooleanField(null=True, blank=True)
    basic_salary = models.DecimalField(max_digits=21, decimal_places=4, null=True, blank=True)
    job_title = models.CharField(max_length=200, null=True, blank=True)
    bank_account = models.ForeignKey(
        "misc.BankAccount",
        on_delete=models.CASCADE,
        related_name="employees",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
