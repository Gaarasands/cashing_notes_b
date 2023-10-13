from django.db import models

class RawMaterial (models.Model):
    name = models.CharField(unique = True, max_length = 200,null = False,error_messages='sorry this Raw Material exists before' )
    quantity = models.IntegerField(null = False,error_messages = {'null':'insert the quantity please'})
    price = models.DecimalField(null = False ,max_digits = 9 ,error_messages = {'null':'insert the price please'},decimal_places = 2)
    details = models.CharField(null = True,max_length=500)
    
    class Meta:
        
        db_table = 'Raw_Material'