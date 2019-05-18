from django.db import models


class TestApi(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)
    release_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

