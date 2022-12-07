from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),


    # deploy bug -> use hash browser??
    path('', TemplateView.as_view(template_name='index.html')),

    path('login', TemplateView.as_view(template_name='index.html')),
    path('register', TemplateView.as_view(template_name='index.html')),
    path('profile', TemplateView.as_view(template_name='index.html')),
    path('shipping', TemplateView.as_view(template_name='index.html')),
    path('payment', TemplateView.as_view(template_name='index.html')),
    path('placeorder', TemplateView.as_view(template_name='index.html')),
    path('order/<str:pk>', TemplateView.as_view(template_name='index.html')),
    path('product/<str:pk>', TemplateView.as_view(template_name='index.html')),
    path('cart/<str:pk>', TemplateView.as_view(template_name='index.html')),
    path('cart', TemplateView.as_view(template_name='index.html')),
    path('admin/userlist', TemplateView.as_view(template_name='index.html')),
    path('admin/user/<str:pk>/edit', TemplateView.as_view(template_name='index.html')),
    path('admin/productlist', TemplateView.as_view(template_name='index.html')),
    path('admin/product/<str:pk>/edit', TemplateView.as_view(template_name='index.html')),
    path('admin/orderlist', TemplateView.as_view(template_name='index.html')),

    path('api/products/', include('base.urls.product_urls')),
    path('api/users/', include('base.urls.user_urls')),
    path('api/orders/', include('base.urls.order_urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)