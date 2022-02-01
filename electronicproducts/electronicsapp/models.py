from django.db import models
from electronicproducts.common_utils import ModelEnum

# Create your models here.
class ProductType(ModelEnum):
    MOBILE = "Mobile"
    LAPTOP = "Laptop"

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class ProductDetail(TimestampedModel):
    name = models.TextField()
    description = models.TextField()
    type = models.CharField(choices=ProductType.get_values(),null=True, blank=True, max_length=55)

    class Meta:
        db_table = "product_details"


class MobileDetail(TimestampedModel):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    processor = models.TextField()
    ram = models.CharField(max_length=100)
    screen_size = models.TextField()
    color = models.CharField(max_length=100)

    class Meta:
        db_table = "mobile_details"


class LaptopDetail(TimestampedModel):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    processor = models.TextField()
    ram = models.CharField(max_length=100)
    hd_capacity = models.TextField()

    class Meta:
        db_table = "laptop_details"
