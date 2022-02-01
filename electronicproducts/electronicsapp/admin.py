from django.contrib import admin
from .models import ProductDetail, LaptopDetail, MobileDetail

# Register your models here.
admin.site.register(ProductDetail)
admin.site.register(MobileDetail)
admin.site.register(LaptopDetail)
