from rest_framework import serializers
from .models import ProductRawMaterial

class ProductRawMaterialSerializer(serializers.ModelSerializer):
    id_rawMaterial = RawMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = ProductRawMaterial
        fields = '__all__'
