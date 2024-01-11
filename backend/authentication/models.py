from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER = (
    ('male','Male'),
    ('female','Female'),
)

# Create your models here.
class CustomUsers(AbstractUser):
    phone=models.CharField(max_length=11,null=True,default=None)
    gender=models.CharField(choices=GENDER,max_length=10,default='male')
    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
