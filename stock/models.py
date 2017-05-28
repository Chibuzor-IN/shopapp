from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    number_available = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
