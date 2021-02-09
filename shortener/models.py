from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=1000)
    short_form = models.CharField(max_length=10)
