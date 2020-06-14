from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

