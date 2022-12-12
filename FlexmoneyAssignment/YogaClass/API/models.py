from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(blank=False)
    batchType = models.CharField(max_length=30, blank=False)
    paymentStatus = models.BooleanField(default=False)