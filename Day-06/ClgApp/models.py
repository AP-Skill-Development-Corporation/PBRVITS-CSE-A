from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	y = {
		(1,'Student'),
		(2,'HOD'),
		(3,'Guest')
	}
	mobile = models.CharField(max_length=50)
	age = models.IntegerField(default=18)
	usrole = models.IntegerField(default=3,choices=y)
	roll = models.CharField(max_length=50)
