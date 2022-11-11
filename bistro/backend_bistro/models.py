from django.db import models

# Create your models here.
class menu_item(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.CharField(max_length=200, null=False, blank=False, unique=True)
    price = models.FloatField()
    spicey_level = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, null=True)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.title

class category(models.Model):
    title = models.CharField(max_length=200, null=True, default=None)

    def __str__(self):
        return self.title


class cuisine(models.Model):
    title = models.CharField(max_length=200, null=True, default=None)

    def __str__(self):
        return self.title