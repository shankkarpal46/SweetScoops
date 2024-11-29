from django.contrib import admin
from .models import Icecream,Category,Tag

# Register your models here.

class Icecream_Admin(admin.ModelAdmin):
    list_display = ['id','icecream_name','icecream_description','icecream_price']

admin.site.register(Icecream,Icecream_Admin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','category_slug']

admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['id','tag_name']

admin.site.register(Tag,TagAdmin)