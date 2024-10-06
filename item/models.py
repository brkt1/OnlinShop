from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Item (models.Model):

    name = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    telegram_link = models.URLField(max_length=200, blank=True )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=' 1')
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField()
    description =  models.TextField(null=False , default='')



    def __str__(self) -> str:
        return self.name
    
