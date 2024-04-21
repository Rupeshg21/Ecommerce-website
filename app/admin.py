from django.contrib import admin
from .models import Sqtable_cont  # Assuming the correct spelling
from .models import *


class SqtableContAdmin(admin.ModelAdmin):
    list_display = ['name', 'gmail', 'msg']  # List fields to display

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'pname',  'price', 'image']  # List fields to display (assuming 'img' is an image field)
    
    def image(self, obj):
        return obj.image.url if obj.image else None



admin.site.register(Sqtable_cont, SqtableContAdmin)  # Register Sqtable_cont model
admin.site.register(Products, ProductAdmin)
     # Register Products model
