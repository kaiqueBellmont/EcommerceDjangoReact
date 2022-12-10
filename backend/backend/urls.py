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
    path('', TemplateView.as_view(template_name='index.html')),

    # TODO problem with browser router react in production
    # way 1: use hash router
    # way 2: deploy the both separated, frond and back (ideal)
    path('login', TemplateView.as_view(template_name='index.html')),
    path('register', TemplateView.as_view(template_name='index.html')),
    path('profile', TemplateView.as_view(template_name='index.html')),
    path('shipping', TemplateView.as_view(template_name='index.html')),
    path('payment', TemplateView.as_view(template_name='index.html')),
    path('placeorder', TemplateView.as_view(template_name='index.html')),
    path('orders/<str:pk>', TemplateView.as_view(template_name='index.html')),
    path('product/<str:pk>', TemplateView.as_view(template_name='index.html')),
    path('cart/<str:pk>', TemplateView.as_view(template_name='index.html')),
    path('cart', TemplateView.as_view(template_name='index.html')),
    path('admin/userlist', TemplateView.as_view(template_name='index.html')),
    path('admin/user/<str:pk>/edit', TemplateView.as_view(template_name='index.html')),
    path('admin/productlist', TemplateView.as_view(template_name='index.html')),
    path('admin/product/<str:pk>/edit', TemplateView.as_view(template_name='index.html')),
    path('admin/orderlist', TemplateView.as_view(template_name='index.html')),

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
