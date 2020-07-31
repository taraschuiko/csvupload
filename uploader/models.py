from django.db import models

# Create your models here.

class Person(models.Model):
  uid = models.CharField(max_length=20)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  birth_day = models.DateField()
  date_change = models.DateField()
  description = models.CharField(max_length=200)