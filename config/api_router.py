from django.conf import settings
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from payroller.company.api.views import CompanyViewSet
from payroller.users.api.views import CustomAuthToken
from payroller.users.api.views import UserViewSet
from payroller.users.api.views import whoami

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("companies", CompanyViewSet, basename="company")

# Create a nested router for employees
companies_router = routers.NestedSimpleRouter(router, r"companies", lookup="company")

urlpatterns = [
    *router.urls,
    path("", include(companies_router.urls)),
    path("login/", CustomAuthToken.as_view(), name="api_token_auth"),
    path("whoami/", whoami, name="whoami"),
]


app_name = "api"
