from django.db import models
# Create your models here.
class Lugat(models.Model):
    english = models.CharField('Inglizcha',max_length=200)
    uzbek = models.CharField('O`zbekcha',max_length=200)