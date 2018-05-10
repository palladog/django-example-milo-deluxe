from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=4)
    text = models.TextField(max_length=400)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
