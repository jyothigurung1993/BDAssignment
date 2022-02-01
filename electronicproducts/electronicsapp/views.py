import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.views import APIView

from .models import ProductDetail, MobileDetail, LaptopDetail


# Create your views here.
""" Creating class to perform CRUD operations on the data"""
""" This class will perform creation of product details and we can fetch all the product details"""
class ElectronicProducts(APIView):
    """
    The below get function will list all the product details.
    It does not take any parameter
    """
    def get(self, request):
        try:
            product_details = ProductDetail.objects.prefetch_related('mobiles', 'laptops').all()
            print(product_details, "@@@@@@@@")
            response = []
            for product in product_details:
                if product.type.upper() == "MOBILE":
                    mobile_detail = product.mobiles.get()
                    product_detail = {
                        'id': product.id,
                        'name': product.name,
                        'type': product.type,
                        'processor': mobile_detail.processor,
                        'ram': mobile_detail.ram,
                        'screen_size': mobile_detail.screen_size,
                        'color': mobile_detail.color
                    }
                    response.append(product_detail)
                elif product.type.upper() == "LAPTOP":
                    laptop_detail = product.laptops.get()
                    product_detail = {
                        'id': product.id,
                        'name': product.name,
                        'type': product.type,
                        'processor': laptop_detail.processor,
                        'ram': laptop_detail.ram,
                        'HD_Capacity': laptop_detail.hd_capacity,
                    }
                    response.append(product_detail)

            return HttpResponse(json.dumps(response), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({
                    'status': 400,
                    'message': "Error: {0}".format(str(e))}))


    """
    The post method is use to create new update records based on type of product
    All the parameters are mandatory
    {
        'name': "Vivo"
        'description': 'The Vivo Y33s smartphone comes with 50MP+2MP+2MP rear camera, 
            16MP front camera, Helio G80 Octa-core processor, 8GB RAM +4GB Extended Ram, 
            128GB ROM, 18W fast charging, 16.71 cm (6.58") with FHD+ Display, 
            5000mAh battery (C-Type) and much more.
        'type': 'mobile'
        'processor': 'Mediatek Helio P35 Processor'
        'ram': '4 GB'
        'screen_size': '6.5 inch'
        'color': 'red'
        'hd_capacity': '1 TB'
    }
    """
    def post(self, request):
        name = request.data.get('name', " ")
        description = request.data.get('description', " ")
        type = request.data.get('type', "")
        processor = request.data.get('processor', "")
        ram = request.data.get('ram', "")
        screen_size = request.data.get('screen_size', "")
        color = request.data.get('color', "")
        hd_capacity = request.data.get('hd_capacity', "")

        if not all([name, description, type]):
            return HttpResponse("Please provide mandatory data: Name, Description and Type", status=400)

        if type.upper() == "MOBILE":
            if not all([processor, ram, screen_size, color]):
                return HttpResponse(json.dumps({"Message": "Please provide additional mandatory data: Processor, RAM, Screen_Size and Color"}), status=400)
        elif type.upper() == "LAPTOP":
            if not all([processor, ram, hd_capacity]):
                return HttpResponse(json.dumps({"Message": "Please provide additional data: Processor, RAM and HD_Capacity"}), status=400)

        try:
            product = ProductDetail(name=name, description=description, type=type)
            product.save()
            if type.upper() == "MOBILE":
                mobile = MobileDetail(product=product, processor=processor, ram=ram, screen_size=screen_size, color=color)
                mobile.save()
            else:
                laptop = LaptopDetail(product=product, processor=processor, ram=ram, hd_capacity=hd_capacity)
                laptop.save()

            return HttpResponse("Success")
        except Exception as e:
            return HttpResponse(json.dumps({
                    'status': 400,
                    'message': "Error: {0}".format(str(e))}))


class ElectronicProduct(APIView):
    """
        The below get function will list the product details of specified product id
        It take product_id as parameter
    """
    def get(self, request, product_id):
        product_id = product_id

        try:
            product = ProductDetail.objects.prefetch_related('mobiles', 'laptops').get(pk=product_id)
            response = []
            if product.type.upper() == "MOBILE":
                mobile_detail = product.mobiles.get()
                product_detail = {
                    'id': product.id,
                    'name': product.name,
                    'type': product.type,
                    'processor': mobile_detail.processor,
                    'ram': mobile_detail.ram,
                    'screen_size': mobile_detail.screen_size,
                    'color': mobile_detail.color
                }
                response.append(product_detail)
            elif product.type.upper() == "LAPTOP":
                laptop_detail = product.laptops.get()
                product_detail = {
                    'id': product.id,
                    'name': product.name,
                    'type': product.type,
                    'processor': laptop_detail.processor,
                    'ram': laptop_detail.ram,
                    'HD_Capacity': laptop_detail.hd_capacity,
                }
                response.append(product_detail)

            return HttpResponse(json.dumps(response), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({
                    'status': 400,
                    'message': "Error: {0}".format(str(e))}))


    """
       The put method is use to update records based on product id
       Not allowed to change the type of product
       {
           'name': "Vivo"
           'description': 'The Vivo Y33s smartphone comes with 50MP+2MP+2MP rear camera, 
               16MP front camera, Helio G80 Octa-core processor, 8GB RAM +4GB Extended Ram, 
               128GB ROM, 18W fast charging, 16.71 cm (6.58") with FHD+ Display, 
               5000mAh battery (C-Type) and much more. 
           'processor': 'Mediatek Helio P35 Processor'
           'ram': '4 GB'
           'screen_size': '6.5 inch'
           'color': 'red'
           'hd_capacity': '1 TB'
       }
       """
    def put(self, request, product_id):
        product_id = product_id
        if not product_id:
            return HttpResponse("Please provide mandatory data", status=400)

        try:
            product = ProductDetail.objects.prefetch_related('mobiles', 'laptops').filter(id=product_id).first()
            if product:
                name = request.data.get('name', None)
                description = request.data.get('description', None)
                type = request.data.get('type', None)
                processor = request.data.get('processor', None)
                ram = request.data.get('ram', None)
                screen_size = request.data.get('screen_size', None)
                color = request.data.get('color', None)
                hd_capacity = request.data.get('hd_capacity', None)

                if name:
                    product.name = name
                    product.save()

                if description:
                    product.description = description
                    product.save()

                if type:
                    return HttpResponse("Your not allowed to change the type of the product", status=400)

                if product.type.upper() == "MOBILE":
                    mobile = product.mobiles.get()
                    if processor:
                        mobile.processor = processor
                        mobile.save()
                    if ram:
                        mobile.ram = ram
                        mobile.save()
                    if screen_size:
                        mobile.screen_size = screen_size
                        mobile.save()
                    if color:
                        mobile.color = color
                        mobile.save()
                else:
                    laptop = product.laptops.get()
                    if processor:
                        laptop.processor = processor
                        laptop.save()
                    if ram:
                        laptop.ram = ram
                        laptop.save()
                    if hd_capacity:
                        laptop.hd_capacity = hd_capacity
                        laptop.save()
            return HttpResponse("Success")
        except Exception as e:
            return HttpResponse(json.dumps({
                    'status': 400,
                    'message': "Error: {0}".format(str(e))}))


    """
        The below delete the product details based on product id
        It does not take any parameter
    """
    def delete(self, request, product_id):
        product_id = product_id
        if not product_id:
            return HttpResponse("Please provide mandatory data", status=400)

        try:
            product = ProductDetail.objects.filter(id=product_id)
            if product:
                product.delete()
                return HttpResponse("Success")
            else:
                return HttpResponse("Un-Successful", status=400)
        except Exception as e:
            return HttpResponse(json.dumps({
                    'status': 400,
                    'message': "Error: {0}".format(str(e))}))
