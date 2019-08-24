from django.db import models
from django.utils import timezone


class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=100, null=True)
    title = models.TextField(blank=True)
    contents = models.TextField(blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    recommends = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100, null=True)
