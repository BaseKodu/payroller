from rest_framework import permissions


class HasCompanyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if there's a company in the request (set by our middleware)
        if not hasattr(request, "company") or not request.company:
            return False

        # Check if the user is authenticated and has access to this company
        is_authenticated = request.user.is_authenticated
        user_companies_exists = request.user.companies.filter(
            id=request.company.id,
        ).exists()
        return is_authenticated and user_companies_exists
