# ruff: noqa: E501

# Create your models here.
from common.mixins import BaseModel
from django.db import models
from django.db.models import F
from djmoney.models.fields import MoneyField


class Earnings(BaseModel):
    basic_salary = MoneyField(max_digits=19, decimal_places=4)
    commission = MoneyField(max_digits=19, decimal_places=4)
    total = models.GeneratedField(
        expression=F("basic_salary") + F("commission"),
        output_field=MoneyField(max_digits=19, decimal_places=4),
        db_persist=True,
    )


class Deductions(BaseModel):
    paye = MoneyField(max_digits=19, decimal_places=4)
    uif = MoneyField(max_digits=19, decimal_places=4)
    medical_aid = MoneyField(max_digits=19, decimal_places=4)
    total = models.GeneratedField(
        expression=F("paye") + F("uif") + F("medical_aid"),
        output_field=MoneyField(max_digits=19, decimal_places=4),
        db_persist=True,
    )


class CompanyContributions(BaseModel):
    uif = MoneyField(max_digits=19, decimal_places=4)
    sdl = MoneyField(max_digits=19, decimal_places=4)
    total = models.GeneratedField(
        expression=F("uif") + F("sdl"),
        output_field=MoneyField(max_digits=19, decimal_places=4),
        db_persist=True,
    )


class Payslip(BaseModel):
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE, related_name="payslips")
    date = models.DateField()
    earnings = models.OneToOneField("Earnings", on_delete=models.CASCADE, related_name="payslip")
    company_contributions = models.OneToOneField(
        "CompanyContributions",
        on_delete=models.CASCADE,
        related_name="payslip",
    )
    deductions = models.OneToOneField("Deductions", on_delete=models.CASCADE, related_name="payslip")

    @property
    def nett_salary(self):
        """
        This shouldve been a GeneratedField but django does not support for fields with references
        """
        return self.earnings.total - self.deductions.total
