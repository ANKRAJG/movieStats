from django.db import models


class Hollywood(models.Model):
    movie = models.CharField(max_length = 140)
    actors = models.TextField()
    directors = models.CharField(max_length = 140)
    producers = models.TextField()
    release = models.IntegerField()
    rating = models.FloatField()
    budget = models.IntegerField()
    box_office = models.IntegerField()
    
    def __str__(self):
        return self.movie

    
    
class Profession(models.Model):
    prof_name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.prof_name

    
    
class Artist(models.Model):
    prof = models.ForeignKey(Profession)
    artist_name = models.CharField(max_length = 40) 
    
    def __str__(self):
        return self.artist_name

    
    
class Xaxis(models.Model):
    xaxis_value = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.xaxis_value
    
  

class Yaxis(models.Model):
    yaxis_value = models.CharField(max_length = 30)

    def __str__(self):
        return self.yaxis_value

    
    
class MovieImage(models.Model):
    movie_name = models.CharField(max_length = 140)
    movie_img = models.ImageField(upload_to = "photos")
    
    def __str__(self):
        return self.movie_name
    

    
class ArtistImage(models.Model):
    artst_name = models.CharField(max_length = 140)
    artist_img = models.ImageField(upload_to = "photos/artist_images")
    artist_prof = models.CharField(max_length = 150)
    artist_gender = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.artst_name