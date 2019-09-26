from django.db import models


class Song(models.Model):
    allSongs = models.TextField( default='null')

    def __str__(self):
        return self.allSongs

class Album(models.Model):
    allAlbums = models.TextField( default='null')
    songs = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.allAlbums



class Artist(models.Model):
    name = models.TextField( default='null')
    albums = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

