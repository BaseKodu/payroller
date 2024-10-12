from rest_framework import serializers

from payroller.employees.models import PaymentMethodChoices
from payroller.misc.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ["accounttype", "bank_name", "account_number", "branch_code", "account_holder_name"]  # noqa: E501

    def clean(self, *args, **kwargs):
        payment_method = self.initial_data.get("payment_method")
        if payment_method != PaymentMethodChoices.EFT:
            message = "Only EFT payment method is allowed for bank accounts."
            raise serializers.ValidationError(message)
        super().clean(*args, **kwargs)
