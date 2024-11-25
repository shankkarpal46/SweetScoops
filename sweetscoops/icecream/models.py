from django.db import models

# Create your models here.
class Icecream(models.Model):
    icecream_name=models.CharField(max_length=100,null=False)
    icecream_description=models.TextField(default="icecream description")
    icecream_price=models.PositiveIntegerField(default=0)
    icecream_image=models.ImageField(upload_to="icecreams/")
    #product_brand=models.CharField(max_length=100,default="superpet")

    #customManager = ProductCustomManager()

    def __str__(self):
        return self.icecream_name