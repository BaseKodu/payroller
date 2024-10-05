from rest_framework import serializers

from payroller.company.models import Company  # Use the full path


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name", "trading_name", "created_by"]
        read_only_fields = ["created_by"]

        extra_kwargs = {
            "url": {"view_name": "api:company-detail", "lookup_field": "pk"},
        }
