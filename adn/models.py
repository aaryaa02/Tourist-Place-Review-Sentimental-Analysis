from django.db import models

# Create your models here.

class datamodel(models.Model):
    City=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Review=models.CharField(max_length=100)
    Rating=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    Raw_Review = models.CharField(max_length=100)