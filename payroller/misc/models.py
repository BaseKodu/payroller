# ruff: noqa: DJ001, E501

from common.mixins import BaseModel
from django.db import models


class AccountTypesChoices(models.TextChoices):
    SAVINGS = "S", "Savings"
    CHEQUE = "C", "Cheque"
    TRANSMISSION = "T", "Transmission"
    CURRENT = "CU", "Current"
    CREDIT = "CR", "Credit"
    OTHER = "O", "Other"


class Address(BaseModel):
    line1 = models.CharField(max_length=200, null=True, blank=True)
    line2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    province = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)


class BankAccount(BaseModel):
    accounttype = models.CharField(choices=AccountTypesChoices.choices, max_length=2)
    bank_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=200)
    account_holder_name = models.CharField(max_length=200)
    other_bank_name = models.CharField(max_length=200)


class Country(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    iso2 = models.CharField(max_length=2, null=True, blank=True)
    iso3 = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name


class Province(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    name_ascii = models.CharField(max_length=100, null=True, blank=True)

    latitude = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)

    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)

    simplemaps_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name
