from django.db import models

# Create your models here.
class numbers(models.Model):
    number = models.IntegerField(primary_key=True)