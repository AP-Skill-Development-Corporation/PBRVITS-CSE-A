from django.db import models

# Create your models here.
class Stdnt(models.Model):
	roll = models.CharField(max_length=50)
	sname = models.CharField(max_length=50)
	year = models.CharField(max_length=50)
