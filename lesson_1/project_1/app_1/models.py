from django.db import models


class Spider(models.Model):
    name = models.CharField("Spider name", max_length=30)
