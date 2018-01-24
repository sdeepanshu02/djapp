from django.db import models

class Menu(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
