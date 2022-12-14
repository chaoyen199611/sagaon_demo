from platform import architecture
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    motivation = models.TextField(blank=True)
    model = models.TextField(blank=True)
    nas = models.TextField(blank=True)
    algorithm = models.TextField(blank=True)
    architecture = models.TextField(blank=True)
    dataset = models.TextField(blank=True)
    experiment = models.TextField(blank=True)
    demo = models.TextField(blank=True)
    future = models.TextField(blank=True)