from django.db import models
from common.mixins import BaseModel


class GenderChoices(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
class Employee(BaseModel):
    title = models.CharField(max_length=200)
    initials = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    other_names = models.CharField(max_length=200)
    dob = models.DateField()
    rsa_id_number = models.CharField(max_length=13, null=True, blank=True)
    passport_number = models.CharField(max_length=20, null=True, blank=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='employees')
    employee_code = models.CharField(max_length=200)
    employment_date = models.DateField()
    gender = models.IntegerField(choices=GenderChoices)
    cell_no = models.CharField(max_length=20)
    work_no = models.CharField(max_length=20)
    #payment_method = models.ForeignKey('common.PaymentMethod', on_delete=models.CASCADE, related_name='employees')
    #bank_account = models.ForeignKey('common.BankAccount', on_delete=models.CASCADE, related_name='employees')
    pays_paye = models.BooleanField()
    pays_uif = models.BooleanField()
    basic_salary = models.DecimalField(max_digits=21, decimal_places=4)
    job_title = models.CharField(max_length=200)
    
    abstract = True
    
    


