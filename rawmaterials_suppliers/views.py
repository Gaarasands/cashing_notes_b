from django.shortcuts import render , HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import SupplierRawmaterialSerializer
from .models import RawmaterialSupplier

@api_view(['POST'])
def add(request):
    data = JSONParser().parse(request)
    serializer = SupplierRawmaterialSerializer(data=data, many=True)    
    if serializer.is_valid():
        serializer.save()
        total = sum(item['material_price'] for item in serializer.data)
        for item in serializer.data:
            del item['total']
            response_data = serializer.data + [{'total': total}]        
        return Response(response_data, status=status.HTTP_201_CREATED)    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getall(request):
    supplier_rawmaterial = RawmaterialSupplier.objects.all()
    serializer = SupplierRawmaterialSerializer(supplier_rawmaterial, many=True)
    return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})


@api_view(['GET'])
def getid(request, id):
    try:
        supplier_rawmaterial = RawmaterialSupplier.objects.get(id=id)
        serializer = SupplierRawmaterialSerializer(supplier_rawmaterial)
        return Response(serializer.data)
    except:
        return HttpResponse("Not Exist")

@api_view(['GET'])
def getname(request, id ):
    try:
        data = RawmaterialSupplier.objects.filter(name = data['name'])
        serializer = SupplierRawmaterialSerializer(data)
        return HttpResponse(serializer.data)

    except:
        return HttpResponse("Not Exist")


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RawmaterialSupplier
from .serializers import SupplierRawmaterialSerializer

@api_view(['PUT'])
def update(request, id):
    try:
        supplier_rawmaterial = RawmaterialSupplier.objects.get(pk=id)
    except RawmaterialSupplier.DoesNotExist:
        return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if isinstance(request.data, list):
        updated_objects = []
        for obj_data in request.data:
            serializer = SupplierRawmaterialSerializer(data=obj_data)
            if serializer.is_valid():
                serializer.save()
                updated_objects.append(serializer.data)
            else:
                result = {
                    'status': 'Error',
                    'errors': serializer.errors
                }
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

        result = {
            'status': 'Updated Successfully',
            'updated_objects': updated_objects
        }
        return Response(result, status=status.HTTP_200_OK)
    
    result = {
        'status': 'Error',
        'errors': 'Invalid data format'
    }
    return Response(result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete (request, id):
    supplier_rawmaterial = RawmaterialSupplier.objects.get(pk = id)
    supplier_rawmaterial.delete()
    result = {
                'status' : 'Done'
            }
    return Response(result, status = status.HTTP_200_OK)


