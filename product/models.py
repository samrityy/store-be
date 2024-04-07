from django.db import models

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=225)
    image = models.ImageField(upload_to="images/")
    rating = models.JSONField()

    def __str__(self):
        return self.title

