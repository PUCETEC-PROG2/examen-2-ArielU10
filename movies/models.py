from django.db import models

# Create your models here.
class Movie(models.Model):
    #id_movie = models.IntegerField(null=False)
    MOVIE_GENRE = {
        ("T", "Terror"),
        ("A", "Accion"),
        ("C", "Comedia"),
        ("D", "Drama"),
    }
    title = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=30, choices=MOVIE_GENRE, null=False)
    director_name = models.CharField(max_length=30, null=False)
    year = models.IntegerField(null=False)
    synopsis = models.TextField(null=False, default="")
    
    def __str__(self) -> str:
        return self.title