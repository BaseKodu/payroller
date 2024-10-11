from rest_framework import authentication
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from payroller.company.api.serializers import CompanySerializer
from payroller.company.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        """
        This view should return a list of all companies
        for the currently authenticated user.
        """
        user = self.request.user
        return Company.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        serializer.instance.created_by.companies.add(serializer.instance)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Company created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
