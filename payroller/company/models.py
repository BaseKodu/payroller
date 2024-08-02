'''
from django.db import models
from common.mixins import BaseModel
class Company(BaseModel):
    name = models.CharField(max_length=200)
    bank_account = models.ForeignKey('common.BankAccount', on_delete=models.CASCADE, related_name='companies')
    address = models.ForeignKey('payslip.Payslip', on_delete=models.CASCADE, related_name='companies')
'''