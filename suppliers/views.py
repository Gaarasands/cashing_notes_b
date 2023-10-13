from django.shortcuts import render , HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import SupplierSerializer
from .models import Supplier


@api_view(['GET'])
def getall(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add(request):
    data = JSONParser().parse(request)
    supplier = SupplierSerializer(data = data)
    if supplier.is_valid():
        supplier.save()
        HttpResponse(supplier, status = status.HTTP_201_CREATED),
        return Response(supplier.errors ,status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getid(request, id):
    try:
        supplier = Supplier.objects.get(id=id)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)
    except:
        return HttpResponse("Not Exist")

@api_view(['GET'])
def getname(request, id ):
    try:
        data = Supplier.objects.filter(name = data['name'])
        serializer = SupplierSerializer(data)
        return HttpResponse(serializer.data)

    except:
        return HttpResponse("Not Exist")

@api_view(['PUT'])
def update(request, id,): 
    data = request.data
    supplier = Supplier.objects.get(pk = id)
    supplierserializer = SupplierSerializer(supplier, data)
    if supplierserializer.is_valid():
        supplierserializer.save()
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
def delete (request, id):
    supplier = Supplier.objects.get(pk = id)
    supplier.delete()
    result = {
                'status' : 'Done'
            }
    return Response(result, status = status.HTTP_200_OK)


