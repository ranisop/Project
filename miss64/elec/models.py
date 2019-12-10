from django.db import models
from django.conf import settings

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

class Home(models.Model):
    name = models.CharField(max_length=50)

class Middle(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    home = models.ForeignKey(Home, on_delete = models.CASCADE)
    middle = models.ForeignKey(Middle, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    # M:N (좋아요 기능) - User:Product
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_products')
    
class Manual(models.Model):
    product = models.OneToOneField(Product, on_delete = models.CASCADE)
    image = models.TextField()
    pdf = models.TextField()