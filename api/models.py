from django.db import models

# Create your models here.

class Song(models.Model):
    album = models.CharField(max_length = 200)
    artist = models.CharField(max_length = 200)
    song_name = models.CharField(max_length = 200)

    def __str__(self):
        return f"album: {self.album}, artist: {self.artist}, song name: {self.song_name}"
