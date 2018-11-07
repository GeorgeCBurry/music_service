from django.conf.urls import url
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rf_views

from .views import ArtistViewSet, AlbumViewSet, SongViewSet


# router = DefaultRouter()
# router.register(r'artists', ArtistViewSet, base_name='artists')
# router.register(r'albums', AlbumViewSet, base_name='albums')
# router.register(r'songs', SongViewSet, base_name='songs')

# urlpatterns = router.urls

urlpatterns = [
    path('artists/', ArtistViewSet.as_view(), name="artists"),
    path('albums/', AlbumViewSet.as_view(), name="albums"),
    path('songs/', SongViewSet.as_view(), name="songs")
]

# urlpatterns += [
#     url(r'^api-token-auth/', rf_views.obtain_auth_token),
# ]