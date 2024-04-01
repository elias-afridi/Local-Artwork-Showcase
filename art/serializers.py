from rest_framework import serializers
from .models import  Artist,Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['id','artist', 'title', 'description', 'creation_date', 'image_url']
        
class ArtistProfileSerializer(serializers.ModelSerializer):
    artwork = ArtworkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id','user', 'name', 'bio', 'artwork']
       
        
        