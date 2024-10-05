from rest_framework.views import exception_handler


def company_aware_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the custom data to the response.
    if response is not None:
        response.data["status_code"] = response.status_code

        # Add company information if available
        request = context.get("request")
        if request and hasattr(request, "company"):
            company = request.company
            if company:
                response.data["company"] = {
                    "id": company.id,
                    "name": company.name,
                    "trading_name": company.trading_name,
                }
            else:
                response.data["company"] = None
        else:
            response.data["company"] = "Not available"

    return response
