from django.db import models


class KufarParser(models.Model):

    link = models.CharField('link here', max_length=124)
