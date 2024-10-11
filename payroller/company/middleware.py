from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

from .models import Company


class CompanyURLMiddleware(MiddlewareMixin):
    """
    Use this middleware to set or retrieve the company_pk from the request object
    """

    def process_request(self, request):
        resolved = resolve(request.path_info)
        company_id = resolved.kwargs.get("company_pk")
        if company_id:
            try:
                request.company = Company.objects.get(id=company_id)
            except Company.DoesNotExist:
                request.company = None
        else:
            request.company = None
