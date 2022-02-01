import json
from django.shortcuts import render
from rest_framework.views import APIView

from django.http import HttpResponse
from .models import ProductDetail, MobileDetail, LaptopDetail
from django.core import serializers

# Create your views here.
""" Creating class to perform CRUD operations on the data"""
class ElectronicProducts(APIView):

    def get(self, request):
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

        product = ProductDetail(name=name, description=description, type=type)
        product.save()
        if type.upper() == "MOBILE":
            mobile = MobileDetail(product=product, processor=processor, ram=ram, screen_size=screen_size, color=color)
            mobile.save()
        else:
            laptop = LaptopDetail(product=product, processor=processor, ram=ram, hd_capacity=hd_capacity)
            laptop.save()

        return HttpResponse("Success")


class ElectronicProduct(APIView):

    def get(self, request, product_id):
        product_id = product_id
        print(product_id)
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


    def put(self, request, product_id):
        product_id = product_id
        if not product_id:
            return HttpResponse("Please provide mandatory data", status=400)
        product = ProductDetail.objects.filter(id=product_id)
        if product:
            if product.type.upper() == "MOBILE":
                return HttpResponse("Success")
            elif product.type.upper() == "LAPTOP":
                return HttpResponse("Success")
        else:
            return HttpResponse("Un-Successful", status=400)

    def delete(self, request, product_id):
        product_id = product_id
        if not product_id:
            return HttpResponse("Please provide mandatory data", status=400)
        product = ProductDetail.objects.filter(id=product_id)
        if product:
            product.delete()
            return HttpResponse("Success")
        else:
            return HttpResponse("Un-Successful", status=400)
