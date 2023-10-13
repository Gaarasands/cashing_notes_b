from rest_framework import serializers
from rawmaterials.models import RawMaterial

class RawMaterialSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    details = serializers.CharField()


    def create(self, validated_data):
        return RawMaterial.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.quantity = validated_data.get('quantity',instance.quantity)
        instance.price = validated_data.get('price',instance.price)
        instance.details = validated_data.get('details',instance.details)
        instance.save(),
        return instance