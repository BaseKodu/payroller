# Register your models here.
from django.contrib import admin

from .models import AgeRange
from .models import SarsFinancialYear
from .models import TaxBracket
from .models import TaxRebate
from .models import TaxThreshold

admin.site.register(SarsFinancialYear)
admin.site.register(AgeRange)
admin.site.register(TaxThreshold)
admin.site.register(TaxBracket)
admin.site.register(TaxRebate)


class TaxBracketAdmin(admin.ModelAdmin):
    list_display = ("pk", "tax_year", "lower_limit", "upper_limit", "rate")
    list_filter = ("tax_year",)


admin.site.unregister(TaxBracket)
admin.site.register(TaxBracket, TaxBracketAdmin)
