from .models import Artist,Artwork
from rest_framework import viewsets
from .serializers import ArtistProfileSerializer,ArtworkSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly,ProfileHolderOrReadOnly


class ArtistDetailViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.prefetch_related('artwork')
    serializer_class = ArtistProfileSerializer
    permission_classes = [IsAuthenticated,ProfileHolderOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    
    
    
