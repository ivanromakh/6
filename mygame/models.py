from __future__ import unicode_literals
from utils import *
from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length = 30)
    strength = models.IntegerField(default = 2)
    intellegent = models.IntegerField(default = 2)
    swiftness = models.IntegerField(default = 2)
    diplonacy = models.IntegerField(default = 2)
    militant = models.IntegerField(default = 2)
    my_image = models.ImageField(upload_to='media')
    def __unicode__(self):
        return self.name



