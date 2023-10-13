from django.shortcuts import render , HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from products.serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def getall(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})


@api_view(['POST'])
def add(request):
    print(request.data)  # Print the received data for debugging
    product = ProductSerializer(data=request.data, context={'request': request})
    if product.is_valid():
        product.save()
        return Response(product.data, status=status.HTTP_201_CREATED, headers={'Access-Control-Allow-Origin': '*'})
    else:
        print(product.errors)  # Print validation errors for debugging
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})

@api_view(['GET'])
def getid(request, id):
    try:
        product = Product.objects.get(id=id)
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)
    except:
        return HttpResponse("Not Exist")

@api_view(['GET'])
def getname(request, id ):
    try:
        data = Product.objects.filter(name = data['name'])
        product_serializer = ProductSerializer(data)
        return HttpResponse(product_serializer.data)   
    except:
        result = {
            'status':'Error'   
                }    
        return Response(result, status = status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request, id): 
    data = request.data
    product = Product.objects.get(pk = id)
    productserializer = ProductSerializer(product, data)
    if productserializer.is_valid():
        productserializer.save()
        result = {
                'status' : 'Done'
            }
        return Response(result, status = status.HTTP_202_ACCEPTED)
    else:
        result = {
            'status':'Error'
            }    
        return Response(result, status = status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete(request, id):
    try:
        product = Product.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
    if product.delete():
        result = {
            'status': 'Product deleted',
            'id': id
        }
        return Response(result, status=status.HTTP_200_OK)
    else:
        result = {
            'error': 'Error in deleting product'
        }
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
