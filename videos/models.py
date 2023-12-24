from django.db import models
import magic
from django.core.exceptions import ValidationError


# Create your models here.
class videos(models.Model):
    """"""
    file = models.FileField()

class search_keywords(models.Model):
    """"""
    search_keyword = models.CharField(max_length=100)
