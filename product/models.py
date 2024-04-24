from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    image = models.URLField()
    rating = models.JSONField()

    def __str__(self):
        return self.title

