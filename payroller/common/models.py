'''
from django.db import models
from common.mixins import BaseModel

class Address(BaseModel):
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)

class PaymentMethod(BaseModel):
    name = models.CharField(max_length=200)

class BankAccount(models.Model):
    accounttype = models.ForeignKey('AccountType', on_delete=models.CASCADE, related_name='bank_accounts')
    bank_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=200)
    account_holder_name = models.CharField(max_length=200)
    other_bank_name = models.CharField(max_length=200)

class AccountType(models.Model):
    name = models.CharField(max_length=200)
'''