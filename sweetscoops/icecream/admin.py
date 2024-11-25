from django.contrib import admin
from .models import Icecream

# Register your models here.

class Icecream_Admin(admin.ModelAdmin):
    list_display = ['id','icecream_name','icecream_description','icecream_price']

admin.site.register(Icecream,Icecream_Admin)