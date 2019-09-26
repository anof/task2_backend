import graphene
from graphene_django.types import DjangoObjectType
from .models import Album, Artist, Song

class ArtistObject(DjangoObjectType):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumObject(DjangoObjectType):
    class Meta:
        model = Album
        fields = '__all__'

class SongObject(DjangoObjectType):
    class Meta:
        model = Song
        fields = '__all__'

class Query(graphene.ObjectType):
    all_artist = graphene.List(ArtistObject)
    all_album = graphene.List(AlbumObject)
    all_song = graphene.List(SongObject)
    
    def resolve_all_artist(self, info):
        return  Artist.objects.all()

    def resolve_all_album(self, info):
        return  Album.objects.all()

    def resolve_all_song(self, info):
        return  Song.objects.all()
