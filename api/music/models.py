from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist_id = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Song(models.Model):
    artist_id = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title