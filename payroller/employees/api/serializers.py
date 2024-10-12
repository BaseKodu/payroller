from rest_framework import serializers

from payroller.employees.models import Employee
from payroller.misc.api.serializers import BankAccountSerializer
from payroller.misc.models import BankAccount


class EmployeeSerializer(serializers.ModelSerializer):
    bank_account = BankAccountSerializer(required=False, allow_null=True)

    class Meta:
        model = Employee
        fields = "__all__"  # List the specific fields you want to include
        read_only_fields = ["company"]  # Make company read-only as it's set in the view

        extra_kwargs = {
            "url": {"view_name": "api:employee-detail", "lookup_field": "pk"},
        }

    def create(self, validated_data):
        bank_account_data = validated_data.pop("bank_account", None)
        if bank_account_data:
            validated_data["bank_account"] = BankAccount.objects.create(**bank_account_data)  # noqa: E501
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        bank_account_data = validated_data.pop("bank_account", None)
        if bank_account_data:
            bank_account_serializer = BankAccountSerializer(instance.bank_account, data=bank_account_data)  # noqa: E501
            if bank_account_serializer.is_valid():
                bank_account_serializer.save()
        return super().update(instance, validated_data)
