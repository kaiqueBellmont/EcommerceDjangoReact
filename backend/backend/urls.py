from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# swagger
from swagger.swagger import schema_view

urlpatterns = [
    # admin paths
    path('admin/', admin.site.urls),
    # deploy with backend, single project
    path('', schema_view.with_ui('swagger'), name="swagger_schema"),

    # base urls
    path('api/products/', include('base.urls.product_urls')),
    path('api/users/', include('base.urls.user_urls')),
    path('api/orders/', include('base.urls.order_urls')),

    # swagger
    path('api/swagger/schema', schema_view.with_ui('swagger'), name="swagger_schema"),
    path('api/swagger/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
