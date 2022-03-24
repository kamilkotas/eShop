from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(default='/static/images/placeholder.png/')

    def __str__(self):
        return self.name