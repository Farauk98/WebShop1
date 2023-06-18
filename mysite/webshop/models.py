from django.db import models

class Artists(models.Model):
    title = models.CharField(max_length=200)
    birth_date = models.DateField()
    death_date = models.DateField()
   
class Painting(models.Model):
    title = models.CharField(max_length=200)
    width = models.FloatField(0)
    height = models.FloatField(0)
    depth = models.FloatField(0)
    artist_id = models.ForeignKey(Artists, on_delete=models.CASCADE)