from rest_framework import authentication
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from payroller.company.permissions import HasCompanyAccess
from payroller.employees.api.serializers import EmployeeSerializer
from payroller.employees.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, HasCompanyAccess]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        """
        This view should return a list opsef all employees
        for the currently authenticated user, for the company
        set in the request.
        """
        user = self.request.user
        return Employee.objects.filter(company__created_by=user)

    def perform_create(self, serializer):
        serializer.save(company=self.request.company)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Employee created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
