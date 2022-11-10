from django.db import models

# Create your models here.
class menu_item(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.CharField(max_length=200, null=False, blank=False, unique=True)
    price = models.FloatField()
    spicey_level = models.IntegerField()
 #   categories = models.ForeignKey('catergories', on_delete=models.CASCADE)
  #  cuisines = models.ForeignKey('cuisines', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class category(models.Model):
    pass
class cuisine(models.Model):
    pass