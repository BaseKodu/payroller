from django.db import models
from django.db.models import Sum, F
from common.mixins import BaseModel, MoneyField

class Payslip(BaseModel):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, related_name='payslips')
    date = models.DateField()
    address = models.ForeignKey('common.Address', on_delete=models.CASCADE, related_name='payslips')
    earnings = models.OneToOneField('Earnings', on_delete=models.CASCADE, related_name='payslip')
    company_contributions = models.OneToOneField('CompanyContributions', on_delete=models.CASCADE, related_name='payslip')
    deductions = models.OneToOneField('Deductions', on_delete=models.CASCADE, related_name='payslip')

class Earnings(BaseModel):
    basic_salary = MoneyField()
    commission = MoneyField()
    total = models.GeneratedField(
        expression= F('basic_salary') + F('commission'),
        output_field=MoneyField(),
        db_persist=True
    )

class Deductions(BaseModel):
    paye = MoneyField()
    uif = MoneyField()
    medical_aid = MoneyField()
    total = models.GeneratedField(
        expression= F('paye') + F('uif') + F('medical_aid'),
        output_field=MoneyField(),
        db_persist=True
    )
class CompanyContributions(BaseModel):
    uif = MoneyField()
    sdl = MoneyField()
    total = models.GeneratedField(
        expression= F('uif') + F('sdl'),
        output_field=MoneyField(),
        db_persist=True
    )