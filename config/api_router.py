from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from payroller.company.api.views import CompanyViewSet
from payroller.users.api.views import CustomAuthToken
from payroller.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("company", CompanyViewSet)

urlpatterns = [
    *router.urls,
    path("login/", CustomAuthToken.as_view(), name="api_token_auth"),
]


app_name = "api"
