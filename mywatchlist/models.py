from django.db import models

# Create your models here.
class Watchlist(models.Model):
    watched = models.BooleanField(default=False)
    title  = models.CharField(max_length=100)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.URLField()

