from django.db import models
from datetime import datetime



class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    

class MoneyField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_digits', 21)
        kwargs.setdefault('decimal_places', 4)
        kwargs.setdefault('default', 0.00)
        super().__init__(*args, **kwargs)