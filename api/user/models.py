from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  username = None
  email = models.EmailField('email address', unique=True)
  first_name = models.CharField('First Name', max_length=255, blank=True,
                                null=False)
  last_name = models.CharField('Last Name', max_length=255, blank=True,
                               null=False)
  role = models.IntegerField(default=0)  # 0=customer, 1=admin

  USERNAME_FIELD = 'email'

  def __str__(self):
    return f"{self.email} - {self.first_name} {self.last_name}"
