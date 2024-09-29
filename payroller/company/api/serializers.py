from rest_framework import serializers

from payroller.company.models import Company  # Use the full path


class CompanySerializer(serializers.ModelSerializer[Company]):
    class Meta:
        model = Company
        fields = ["name", "trading_name"]

        extra_kwargs = {
            "url": {"view_name": "api:company-detail", "lookup_field": "pk"},
        }
