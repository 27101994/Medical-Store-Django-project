from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
# from django.db import models
# from django.contrib.auth.models import User

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add additional fields specific to your Customer model, if needed
#     # For example: name, email, phone, etc.



