from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=10)
    concern=models.TextField()

