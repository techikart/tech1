from django.db import models

# Create your models here.
class product_details(models.Model):
    product_number = models.TimeField()
    product_name = models.CharField(max_length=50)
    product_type = models.TextField()
    product_mrp = models.TextField()
    product_description = models.TextField()
    product_img = models.TextField()
    
    def _str_(self):
        return self.product_name
    
