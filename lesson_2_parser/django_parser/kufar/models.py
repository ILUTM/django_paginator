from django.db import models


class Furniture(models.Model):
    link = models.TextField("Link to Furniture")
    description = models.TextField(
        verbose_name="Description of Furniture"
    )
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Price")
    parse_datetime = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name="date of coming"
    )

    def get_absolute_url(self):
        return self.link

    class Meta:
        verbose_name = "Mieblia"
        verbose_name_plural = "Meblia"
        ordering = ["parse_datetime","price"]

    def __str__(self):
        return f"description: {self.description} | {self.price}"

