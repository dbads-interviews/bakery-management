from django.db import models

# Create your models here.


class Product(models.Model):
  name = models.CharField(max_length=50, blank=True)
  price = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return self.name
