from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
  
    def __str__(self):
        return self.name
    
 
class Customer:
    def __init__(self, name, email, contactnumber):
        self.name = name
        self.email = email
        self.contactnumber = contactnumber
     
    def __str__(self):
        return f"{self.name}"