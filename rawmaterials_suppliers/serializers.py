from rest_framework import serializers
from .models import RawmaterialSupplier

class SupplierRawmaterialSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    material_price = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = RawmaterialSupplier
        fields = ['id','id_supp', 'id_raw', 'price', 'quantity', 'material_price', 'total']

    def get_material_price(self, obj):
        return obj.material_price

    def get_total(self, obj):
        return obj.material_price
        
    def create(self, validated_data):
        instance = RawmaterialSupplier.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
