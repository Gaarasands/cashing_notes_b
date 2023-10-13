from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False,
                            error_messages={
                                'unique': 'This product name already exists.',
                                'null': 'Please enter a product name.',
                                'max_length': 'The field must be less than 200 characters long.'
                            })
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    details = models.CharField(max_length=240, null=True)
    image = models.ImageField(null=True ,blank = True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product'