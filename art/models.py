from django.db import models
from account.models import User

# Create your models here.

class Artist(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='artist')
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class Artwork(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,related_name='artwork')
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    creation_date = models.DateField()
    image_url = models.URLField()
    
    def __str__(self):
        return self.title
    

