from rest_framework import serializers
from .models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.StringRelatedField(many=True)
    songs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Artist
        fields = ('pk', 'name', 'albums', 'songs')


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ('pk', 'name', 'artist_id', 'songs')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('pk', 'title', 'album_id', 'artist_id')