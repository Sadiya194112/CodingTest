from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView
from product.views.product import *

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('update/<int:pk>/', ProductVariantPriceUpdateView.as_view(), name='edit.product'),
    path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),

    # API
    path('api/products/create/', ProductListAPI.as_view(), name='product_create_api'),
    path('api/products_variant/', ProductVariantListAPI.as_view(), name='product_variant_api'),
    path('api/products_variant_price/', ProductVariantPriceAPI.as_view(), name='product_variant_price_api'),
    path('api/products_variant_image/', ProductImageAPI.as_view(), name='product_variant_image_api'),

]