from django.db import models
from django.contrib.auth import get_user_model

class Url(models.Model):
    url = models.CharField(max_length=1000)
    short_form = models.CharField(max_length=10)
    creator = models.ForeignKey(get_user_model(), blank=True, default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.url} created by {self.creator}'
