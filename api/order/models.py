from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  total = models.IntegerField(null=True, blank=True)
  items = models.CharField(max_length=300)

  def __str__(self):
    return self.user.username


@receiver(pre_save, sender=Order)
def my_callback(sender, instance, *args, **kwargs):
  item_ids = [int(id) for id in instance.items.split(',')]
  products = Product.objects.filter(id__in=item_ids).only('id')
  total = 0
  for product in products:
    total += product.price
  instance.total = total
