from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)   
    name = serializers.CharField()
    number = serializers.CharField()
    type = serializers.CharField()
    location = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Supplier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.number = validated_data.get('number',instance.number)
        instance.details = validated_data.get('details',instance.details)
        instance.type = validated_data.get('type',instance.type)
        instance.location = validated_data.get('location',instance.location)
        instance.email = validated_data.get('email',instance.email)
        instance.save(),
        return instance