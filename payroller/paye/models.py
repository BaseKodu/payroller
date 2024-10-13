# ruff: noqa: DJ001, E501
# Create your models here.
from common.mixins import BaseModel
from django.db import models
from djmoney.models.fields import MoneyField


class MonthOptions(models.TextChoices):
    JANUARY = "Jan", "January"
    FEBRUARY = "Feb", "February"
    MARCH = "Mar", "March"
    APRIL = "Apr", "April"
    MAY = "May", "May"
    JUNE = "Jun", "June"
    JULY = "Jul", "July"
    AUGUST = "Aug", "August"
    SEPTEMBER = "Sep", "September"
    OCTOBER = "Oct", "October"
    NOVEMBER = "Nov", "November"
    DECEMBER = "Dec", "December"


class SarsFinancialYear(BaseModel):
    year = models.IntegerField(unique=True)
    month_start = models.CharField(max_length=3, choices=MonthOptions.choices, default=MonthOptions.MARCH)
    month_end = models.CharField(
        max_length=3,
        choices=MonthOptions.choices,
        default=MonthOptions.FEBRUARY,
    )  # March to February is the default for SARS.

    def __str__(self):
        return f"{self.year} ({self.month_start} to {self.month_end})"

    class Meta:
        ordering = ["year"]


class AgeRange(BaseModel):
    """
    Age ranges for tax thresholds.
    Please note that the age range is inclusive of the from_age and inclusive of the to_age.
    """

    from_age = models.IntegerField()
    to_age = models.IntegerField()

    def __str__(self):
        return f"{self.from_age} to {self.to_age}"


class TaxThreshold(BaseModel):
    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE)
    tax_year = models.ForeignKey(SarsFinancialYear, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=4)

    def __str__(self):
        return f"{self.age_range} - {self.tax_year} - {self.amount}"

    class Meta:
        unique_together = ("age_range", "tax_year")


class TaxBracket(BaseModel):
    tax_year = models.ForeignKey(SarsFinancialYear, on_delete=models.CASCADE)
    lower_limit = MoneyField(max_digits=19, decimal_places=4)
    upper_limit = MoneyField(max_digits=19, decimal_places=4, null=True, blank=True)
    rate = models.DecimalField(max_digits=5, decimal_places=4)
    fixed_amount = MoneyField(max_digits=19, decimal_places=4, null=True, blank=True)

    def __str__(self):
        return f"{self.tax_year} : {self.lower_limit} to {self.upper_limit} - {self.rate * 100}%,  Fixed Amount: {self.fixed_amount}"

    class Meta:
        ordering = ["lower_limit"]

    # TODO: Come back to this validation.
    """
    def _validate_bracket_ranges(self):
        from django.core.exceptions import ValidationError
        from django.db.models import Q

        # Check if there's only one null upper_limit for the tax year
        null_upper_limits = TaxBracket.objects.filter(+
            tax_year=self.tax_year,
            upper_limit__isnull=True
        ).exclude(pk=self.pk).count()

        if self.upper_limit is None and null_upper_limits > 0:
            raise ValidationError("There can only be one tax bracket with a null upper limit per tax year.")

        # Check for gaps or overlaps in ranges
        brackets = list(TaxBracket.objects.filter(tax_year=self.tax_year).exclude(pk=self.pk).order_by('lower_limit'))
        brackets.append(self)
        brackets.sort(key=lambda x: x.lower_limit)

        for i in range(len(brackets) - 1):
            current = brackets[i]
            next_bracket = brackets[i + 1]

            if current.upper_limit != next_bracket.lower_limit:
                raise ValidationError(f"Gap or overlap detected between tax brackets. "
                                      f"{current.upper_limit} should equal {next_bracket.lower_limit}")

        # Ensure the last bracket has a null upper_limit
        if brackets[-1].upper_limit is not None:
            raise ValidationError("The highest tax bracket should have a null upper limit.")

    @classmethod
    def validate_tax_year(cls, tax_year):
        from django.core.exceptions import ValidationError

        brackets = list(cls.objects.filter(tax_year=tax_year).order_by('lower_limit'))

        if not brackets:
            return  # No brackets for this tax year, nothing to validate

        # Check if there's exactly one null upper_limit
        null_upper_limits = sum(1 for bracket in brackets if bracket.upper_limit is None)
        if null_upper_limits != 1:
            raise ValidationError(f"Tax year {tax_year} should have exactly one tax bracket with a null upper limit.")

        # Check for gaps or overlaps
        for i in range(len(brackets) - 1):
            current = brackets[i]
            next_bracket = brackets[i + 1]

            if current.upper_limit != next_bracket.lower_limit:
                raise ValidationError(f"Gap or overlap detected in tax year {tax_year} between tax brackets. "
                                      f"{current.upper_limit} should equal {next_bracket.lower_limit}")

        # Ensure the first bracket starts from 0
        if brackets[0].lower_limit != 0:
            raise ValidationError(f"The lowest tax bracket for tax year {tax_year} should start from 0.")

        # Ensure the last bracket has a null upper_limit
        if brackets[-1].upper_limit is not None:
            raise ValidationError(f"The highest tax bracket for tax year {tax_year} should have a null upper limit.")
    """


class TaxRebate(BaseModel):
    """
    Not sure what these are for, but its fine if we have it. Will have to read up more on them.
    """

    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE)
    tax_year = models.ForeignKey(SarsFinancialYear, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=19, decimal_places=4)

    def __str__(self):
        return f"{self.age_range} - {self.tax_year} - {self.amount}"
