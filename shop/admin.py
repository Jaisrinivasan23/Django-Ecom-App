from django.contrib import admin
from .models import *

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','desc','created_at')
    
admin.site.register(Catageory,CatagoryAdmin)
admin.site.register(Product)
