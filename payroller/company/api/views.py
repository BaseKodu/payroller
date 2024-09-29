from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from payroller.company.api.serializers import CompanySerializer
from payroller.company.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all companies
        for the currently authenticated user.
        """
        user = self.request.user
        return Company.objects.filter(owner=user)
