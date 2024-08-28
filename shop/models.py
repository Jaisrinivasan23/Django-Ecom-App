from django.db import models
import datetime as dt
import os

def getfilename(request, filename):
    now_time = dt.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = "{0}{1}".format(now_time, filename)
    return os.path.join('upload/', file_name)

class Catageory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getfilename, null=True, blank=True)
    desc = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    Catageory = models.ForeignKey(Catageory,on_delete=models.CASCADE)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    pro_image = models.ImageField(upload_to=getfilename, null=True, blank=True)
    desc = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False,help_text="0-Show,1-Hidden")
    original_price = models.FloatField(null=False,blank=False)
    sell_P = models.FloatField(null=False,blank=False)
    trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name