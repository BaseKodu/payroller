from rest_framework import permissions


class HasCompanyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if there's a company in the request (set by our middleware)
        if not hasattr(request, "company") or not request.company:
            return False

        # Check if the user is authenticated and has access to this company
        return request.user.is_authenticated and request.user.companies.filter(id=request.company.id).exists()  # noqa: E501
