# Create your models here.

from common.mixins import BaseModel
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(BaseModel):
    name = models.CharField(
        _("Name of company"),
        max_length=150,
        null=False,
        blank=False,
    )
    trading_name = models.CharField(
        _("Trading Name"),
        max_length=150,
        blank=True,
    )
    created_by = models.ForeignKey("users.User", null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        if not self.trading_name:
            self.trading_name = self.name

        return super().save()

    def get_absolute_url(self) -> str:
        """Get URL for company's detail view.

        Returns:
            str: URL for company detail.

        """
        from django.urls import reverse

        return reverse("company:detail", kwargs={"pk": self.pk})

    def clean(self) -> None:
        super().clean()
        if not self.created_by:
            error = "Cannot created this company without referencing the account that made it"  # noqa: E501
            raise ValidationError(error)


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


class PayrollPeriod(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_day = models.DateField()
    end_day = models.DateField()
    default_start_day = models.DateField(default=1)
    default_end_day = models.DateField(default=31)

    def __str__(self) -> str:
        return f"{self.start_day} - {self.end_day}"


class PaymentPeriods(models.TextChoices):
    MONTHLY = "M", _("Monthly")
    # WEEKLY = "W", _("Weekly") # noqa: ERA001
    # BIWEEKLY = "BW", _("Bi-Weekly") # noqa: ERA001
    # SEMI_MONTHLY = "SM", _("Semi-Monthly") # noqa: ERA001
    # ANNUALLY = "A", _("Annually") # noqa: ERA001
    # DAILY = "D", _("Daily") # noqa: ERA001

    # Add other days here


class WeekendHolidayBehavior(models.TextChoices):
    PAY_ON = "PO", _("Pay on weekend/holiday")
    PAY_BEFORE = "PB", _("Pay before weekend/holiday")
    PAY_AFTER = "PA", _("Pay after weekend/holiday")


class CompanyPayrollSettings(BaseModel):
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        related_name="settings",
    )
    payment_period = models.CharField(
        max_length=2,
        choices=PaymentPeriods.choices,
        default=PaymentPeriods.MONTHLY,
    )

    # For monthly payments
    monthly_payment_day = models.IntegerField(
        default=25,
        help_text=_("Day of the month for payment. Use negative numbers for end-of-month counting."),  # noqa: E501
    )

    # For weekly/bi-weekly payments
    weekly_payment_day = models.IntegerField(
        choices=[
            (0, _("Monday")),
            (1, _("Tuesday")),
            (2, _("Wednesday")),
            (3, _("Thursday")),
            (4, _("Friday")),
            (5, _("Saturday")),
            (6, _("Sunday")),
        ],
        null=True,
        blank=True,
    )

    # For semi-monthly payments
    semi_monthly_first_day = models.IntegerField(
        default=1,
        help_text=_("First payment day for semi-monthly payments"),
    )
    semi_monthly_second_day = models.IntegerField(
        default=15,
        help_text=_("Second payment day for semi-monthly payments"),
    )

    # Common settings
    pay_on_weekends_holidays = models.BooleanField(
        default=False,
        help_text=_("Whether to make payments on weekends and public holidays"),
    )
    weekend_holiday_behavior = models.CharField(
        max_length=2,
        choices=WeekendHolidayBehavior.choices,
        default=WeekendHolidayBehavior.PAY_BEFORE,
        help_text=_("Behavior when payment falls on a weekend or holiday"),
    )

    # Handling months with fewer days
    short_month_behavior = models.CharField(
        max_length=2,
        choices=WeekendHolidayBehavior.choices,
        default=WeekendHolidayBehavior.PAY_BEFORE,
        help_text=_("Behavior when payment day doesn't exist in a shorter month"),
    )
