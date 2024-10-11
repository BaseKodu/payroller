from rest_framework import serializers

from payroller.employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"  # List the specific fields you want to include
        read_only_fields = ["company"]  # Make company read-only as it's set in the view

        extra_kwargs = {
            "url": {"view_name": "api:employee-detail", "lookup_field": "pk"},
        }
