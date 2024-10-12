# Register your models here.
from django.contrib import admin

from .models import Address
from .models import BankAccount
from .models import City
from .models import Country
from .models import Province

admin.site.register(Address)
admin.site.register(BankAccount)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)


class CountryAdmin(admin.ModelAdmin):
    ordering = ("name",)


admin.site.unregister(Country)
admin.site.register(Country, CountryAdmin)
