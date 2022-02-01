from django.shortcuts import render
from rest_framework.views import APIView

from django.http import HttpResponse

# Create your views here.
""" Creating class to perform CRUD operations on the data"""
class ElectronicProducts(APIView):

    def get(self, request):
        print(request)


class ElectronicProduct(APIView):

    def get(self, request):
        print(request)

    def post(self, request):
        print(request)

    def put(self, request):
        print(request)

    def delete(self, request):
        print(request)
