from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", album="", artist=""):
        if title != "" and album != "" and artist != "":
            Artist.objects.create(name=artist)
            Album.objects.create(artist_id=Artist.objects.get(name=artist), name=album)
            Song.objects.create(artist_id=Artist.objects.get(name=artist), album_id=Album.objects.get(name=album), title=title)


    def setUp(self):
        # add test data
        self.create_song("Dreams", "Rumours", "Fleetwood Mac")
        self.create_song("Thriller", "Thriller", "Michael Jackson")
        self.create_song("Time", "The Dark Side of the Moon", "Pink Floyd")
        self.create_song("Hotel California", "Hotel California", "Eagles")
        self.create_song("Stairway to Heaven", "Led Zeppelin IV", "Led Zeppelin")


class GetAllArtistsTest(BaseViewTest):

    def test_get_all_artists(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("artists")
        )

        expected = Artist.objects.all()
        serialized = ArtistSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs")
        )

        # fetch the data from db
        expected = Song.objects.all()
        serialized = SongSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)