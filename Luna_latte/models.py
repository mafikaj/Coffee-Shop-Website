from django.db import models

# Create your models here.
# lunalatte/models.py


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
