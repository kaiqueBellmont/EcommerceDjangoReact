from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="Eukiak documentation"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


