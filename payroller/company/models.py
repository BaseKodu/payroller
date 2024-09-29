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
