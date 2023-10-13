from django.shortcuts import render , HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rawmaterials.serializers import RawMaterialSerializer
from .models import RawMaterial


@api_view(['POST'])
def add(request):
    raw_material = RawMaterialSerializer(data=request.data, context={'request': request})
    if raw_material.is_valid():
        raw_material.save()
        return HttpResponse(raw_material, status = status.HTTP_201_CREATED , headers={'Access-Control-Allow-Origin': '*'})
    else:
        return Response(raw_material.errors ,status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': '*'})

@api_view(['GET'])
def getall(request):
    rawmaterials = RawMaterial.objects.all()
    serializer = RawMaterialSerializer(rawmaterials, many=True)
    return Response(serializer.data, headers={'Access-Control-Allow-Origin': '*'})



@api_view(['GET'])
def getid(request, id):
    try:
        raw_material = RawMaterial.objects.get(id=id)
        raw_material_serializer = RawMaterialSerializer(raw_material)
        return Response(raw_material_serializer.data)
    except:
        return HttpResponse("Not Exist")

@api_view(['GET'])
def getname(request, id ):
    try:
        data = RawMaterial.objects.filter(name = data['name'])
        raw_material_serializer = RawMaterialSerializer(data)
        return HttpResponse(raw_material_serializer.data)   
    except:
        result = {
            'status':'Error'
                }    
        return Response(result, status = status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request, id): 
    data = request.data
    rawmaterial = RawMaterial.objects.get(pk = id)
    rawmaterialserializer = RawMaterialSerializer(rawmaterial, data)
    if rawmaterialserializer.is_valid():
        rawmaterialserializer.save()
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
    raw_material = RawMaterial.objects.get(pk = id)
    if raw_material.delete():
        result = {
                'status' : 'Done'
            }
        return Response(result, status = status.HTTP_200_OK)

    else:
        result = {
            'status' : 'Error in deleting'
        }
        return Response(result, status = status.HTTP_406_NOT_ACCEPTABLE)



