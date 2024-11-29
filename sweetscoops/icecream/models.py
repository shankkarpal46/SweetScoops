from django.db import models
from autoslug import AutoSlugField

#Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100,null=False)
    category_slug = AutoSlugField(populate_from="category_name",unique=True)
    category_image = models.ImageField(upload_to="category/",default="")

    def __str__(self):
        return self.category_name
            
class Icecream(models.Model):
    icecream_name=models.CharField(max_length=100,null=False)
    icecream_description=models.TextField(default="icecream description")
    icecream_price=models.PositiveIntegerField(default=0)
    icecream_image=models.ImageField(upload_to="icecreams/")
    #product_brand=models.CharField(max_length=100,default="superpet")

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    #customManager = ProductCustomManager()

    def __str__(self):
        return self.icecream_name
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=100,null=False)
    icecreams = models.ManyToManyField(Icecream)