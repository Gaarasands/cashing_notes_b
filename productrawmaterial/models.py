from django.db import models
from rawmaterials.models import RawMaterial
from products.models import Product

class ProductRawMaterial (models.Model):
    id_rawMaterial = models.ForeignKey(RawMaterial,on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity_used = models.IntegerField(null=False)