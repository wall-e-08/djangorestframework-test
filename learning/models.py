from django.db import models


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    page = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

