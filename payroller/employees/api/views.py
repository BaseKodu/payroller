from rest_framework import authentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from payroller.employees.api.serializers import EmployeeSerializer
from payroller.employees.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        """
        This view should return a list of all employees
        for the currently authenticated user.
        """
        user = self.request.user
        return Employee.objects.filter(company__created_by=user)

    def perform_create(self, serializer):
        serializer.save(company=self.request.company)
