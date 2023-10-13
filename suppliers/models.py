from django.db import models

class Supplier (models.Model):
    name = models.CharField(max_length = 50,null=False,blank = False)
    number = models.CharField(max_length = 14,unique = True)
    details = models.TextField(null = True)
    type = models.CharField(max_length = 25)
    location = models.CharField(max_length = 200, null = True)
    email = models.EmailField(max_length = 254,unique=True)

    class Meta:
        db_table = 'Supplier'