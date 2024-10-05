# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company


class SetCurrentCompanyView(APIView):
    def post(self, request):
        company_id = request.data.get("company_id")
        if not company_id:
            return Response({"error": "company_id is required"}, status=status.HTTP_400_BAD_REQUEST)  # noqa: E501

        try:
            company = request.user.companies.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"error": "Invalid company_id"}, status=status.HTTP_400_BAD_REQUEST)  # noqa: E501

        request.session["current_company_id"] = company.id
        return Response({"message": f"Current company set to {company.name}"})
