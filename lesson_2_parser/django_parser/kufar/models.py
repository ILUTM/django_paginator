from django.db import models


class Furniture(models.Model):
    link = models.TextField("Link to Furniture")
    description = models.TextField("Description of Furniture")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Price")

