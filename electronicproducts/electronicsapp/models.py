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

    def __str__(self):
        return self.name+" - "+self.type


class MobileDetail(TimestampedModel):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    processor = models.TextField()
    ram = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    class Meta:
        db_table = "mobile_details"
        default_related_name = 'mobiles'

    def __str__(self):
        return self.product.name+"-"+self.color

    @classmethod
    def get_mobile_details(cls, product):
        return MobileDetail.objects.select_related('product').filter(product=product).first

    @classmethod
    def get_mobile_details_by_product_id(cls, product_id):
        return MobileDetail.objects.select_related('product').filter(product_id=product_id).first


class LaptopDetail(TimestampedModel):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    processor = models.TextField()
    ram = models.CharField(max_length=100)
    hd_capacity = models.CharField(max_length=100)

    class Meta:
        db_table = "laptop_details"
        default_related_name = 'laptops'

    def __str__(self):
        return self.product.name+ "-" +self.hd_capacity

    @classmethod
    def get_laptop_details(cls, product):
        return LaptopDetail.objects.select_related('product').filter(product=product).first

    @classmethod
    def get_mobile_details_by_product_id(cls, product_id):
        return MobileDetail.objects.select_related('product').filter(product_id=product_id).first
