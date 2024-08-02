'''
from django.db import models
from common.mixins import BaseModel

class Employee(BaseModel):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    other_names = models.CharField(max_length=200)
    dob = models.DateField()
    rsa_id_number = models.CharField(max_length=13, null=True, blank=True)
    passport_number = models.CharField(max_length=20)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='employees')
    director = models.CharField(max_length=200)
    employee_code = models.CharField(max_length=200)
    employment_date = models.DateField()
    title = models.CharField(max_length=200)
    gender = models.IntegerField()
    cell_no = models.CharField(max_length=200)
    work_no = models.CharField(max_length=200)
    payment_method = models.ForeignKey('common.PaymentMethod', on_delete=models.CASCADE, related_name='employees')
    bank_account = models.ForeignKey('common.BankAccount', on_delete=models.CASCADE, related_name='employees')
    pays_paye = models.BooleanField()
    pays_uif = models.BooleanField()
    initials = models.CharField(max_length=200)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_title = models.CharField(max_length=200)
    
    abstract = True


'''