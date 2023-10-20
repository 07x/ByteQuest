from django.shortcuts import render
from django.http import HttpResponse



# API's IMPORT 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  * 

import requests  

from .serializers import productSerializer

# Create your views here.
def index(request):
    return render(request, 'home.html')


# GET / POST 
class ProductList(APIView):

    # GET 
    def get(self,request):
        product_objs = Product.objects.all()
        serializers = productSerializer(product_objs,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # POST 
    def post(self,request):
        data = request.data  
        serializers = productSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors,status=400)
    
# GET / PUT / DELETE 
class ProductById(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None

    # GET
    def get(self, request, id):
        product = self.get_object(id)
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = productSerializer(product)
        return Response(serializers.data, status=status.HTTP_200_OK)


    # PUT 
    def put(self,request,id):
        product = self.get_object(id)

        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
                
        data = request.data 
        product = Product.objects.get(id=id)
        serializers = productSerializer(product,data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=400)


    # DELETE 
    def delete(self,request,id):
        product = self.get_object(id)
        if not product:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializers = productSerializer(product)
        product.delete()
        return Response(serializers.data, status=status.HTTP_200_OK)
