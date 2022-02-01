from django.urls import path, re_path
from .views import ElectronicProduct, ElectronicProducts

urlpatterns = [
    path('products/', ElectronicProducts.as_view()),
    re_path('product/(?P<product_id>[0-9a-z])/?$', ElectronicProduct.as_view())
]