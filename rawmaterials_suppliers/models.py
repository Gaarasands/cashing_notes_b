from django.db import models
from suppliers.models import Supplier
from rawmaterials.models import RawMaterial

class RawmaterialSupplier(models.Model):
    id_supp = models.ForeignKey(Supplier, on_delete = models.CASCADE,null=False)
    id_raw = models.ForeignKey(RawMaterial, on_delete = models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'Rawmaterial_supplier'

    @property
    def material_price(self):
        return self.price * self.quantity
