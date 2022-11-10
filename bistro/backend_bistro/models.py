from django.db import models

# Create your models here.
class menu_item(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.CharField(max_length=200, null=False, blank=False, unique=True)
    price = models.FloatField()
    spicey_level = models.IntegerField()
        
    
class category(models.Model):

class cuisine(models.Model):