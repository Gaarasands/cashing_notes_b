from products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    image = serializers.ImageField()
    details = serializers.CharField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)
        instance.details = validated_data.get('details',instance.details)
        instance.image = validated_data.get('image',instance.image)

        instance.save(),
        return instance
