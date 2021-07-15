from django.db import models

# Create your models here.
class User(models.Model):
  jtitle = models.CharField(max_length=70)
  cname = models.CharField(max_length=70)
  eto=models.FloatField()
  efrom=models.FloatField()
  sto=models.FloatField()
  sfrom=models.FloatField()
  location=models.CharField(max_length=70)
  dec= models.TextField()