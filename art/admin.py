from django.contrib import admin
from art.models import Artist,Artwork

# Register your models here.
class ArtistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','bio']
    
class ArtworkModelAdmin(admin.ModelAdmin):
    list_display = ['id','artist','title','description','creation_date','image_url']
    
admin.site.register(Artist,ArtistModelAdmin)
admin.site.register(Artwork,ArtworkModelAdmin)
