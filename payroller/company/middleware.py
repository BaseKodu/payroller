from company.models import Company
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin


class CompanyURLMiddleware(MiddlewareMixin):
    def process_request(self, request):
        resolved = resolve(request.path_info)
        company_id = resolved.kwargs.get("company_id")
        if company_id:
            try:
                request.company = Company.objects.get(id=company_id)
            except Company.DoesNotExist:
                request.company = None
        else:
            request.company = None
