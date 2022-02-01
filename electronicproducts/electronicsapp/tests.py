from django.test import TestCase
from django.urls import reverse
from .models import ProductDetail, MobileDetail, LaptopDetail
from .views import ElectronicProducts, ElectronicProduct

# Create your tests here.
class TestElectronicProducts(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ProductDetail.objects.create(name='Redmi 6', description='Redmi new model of cell for demo purpose', type='mobile')

    def test_create_mobile(self):
        product = ProductDetail.objects.get(id=1)
        MobileDetail.objects.create(product=product, processor="xyz", ram="2gb", screen_size="16*15", color="blue")
        mobile = MobileDetail.objects.get(product_id=1)
        self.assertEqual(mobile.color, 'blue')

    def test_create_laptop(self):
        product = ProductDetail.objects.get(id=1)
        LaptopDetail.objects.create(product=product, processor="xyz", ram="2gb", hd_capacity="500gb")
        laptop = LaptopDetail.objects.get(product_id=1)
        self.assertEqual(laptop.ram, '2gb')

    def test_name_label(self):
        product = ProductDetail.objects.get(id=1)
        self.assertEqual(product.name, 'Redmi 6')

    def test_product_type(self):
        product = ProductDetail.objects.get(id=1)
        self.assertEqual(product.type.upper(), "MOBILE")


class ElectronicProductsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_products = 10

        for product_id in range(number_of_products):
            ProductDetail.objects.create(
                name=f'Vivo {product_id}',
                description=f'vivo 8 {product_id}',
                type=f'mobile {product_id}',
            )

    def test_view_url_exists(self):
        response = self.client.get('electronics/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_for_product(self):
        response = self.client.get(reverse('electronics/product/1)'))
        self.assertEqual(response.status_code, 200)