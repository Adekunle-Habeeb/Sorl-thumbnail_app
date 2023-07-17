from django.db import models
from sorl.thumbnail import ImageField


class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=True)
    image = ImageField()
