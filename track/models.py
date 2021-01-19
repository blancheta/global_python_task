from django.db import models


class Artist(models.Model):
    name = models.CharField(unique=True, max_length=80)


class Track(models.Model):

    title = models.CharField(max_length=100)
    duration = models.DecimalField(decimal_places=1, max_digits=4)
    external_id = models.IntegerField(unique=True)
    last_play = models.DateTimeField()
    artists = models.ManyToManyField(Artist, blank=True)
