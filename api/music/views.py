from rest_framework import viewsets
from rest_framework import generics
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistViewSet(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer