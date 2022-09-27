from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    motivation = models.TextField(blank=True)
    model = models.TextField(blank=True)
    dataset = models.TextField(blank=True)
    experiment = models.TextField(blank=True)