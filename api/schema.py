from graphene_django import DjangoObjectType
from .models import SongModel
import graphene

class Song(DjangoObjectType):
    class Meta:
        model = SongModel

class Query(graphene.ObjectType):
    song = graphene.Field(Song, name= graphene.String(), artist= graphene.String(), album= graphene.String())
    songs = graphene.List(Song)

    artists = graphene.List(graphene.String)
    albums = graphene.List(graphene.String, artist=graphene.String())

    def resolve_albums(self, info, **kwargs):
        artist = kwargs.get('artist')

        albums_query = SongModel.objects.filter(artist=artist).values('album').distinct()
        albums_list = []
        for album in albums_query:
            albums_list.append(album['album'])
        return albums_list

    def resolve_artists(self, info, **kwargs):
        artists_query = SongModel.objects.values('artist').distinct()
        artists_list = []
        for artist in artists_query :
            artists_list.append(artist['artist'])
        return artists_list

    def resolve_song (self, info, **kwargs):
        name = kwargs.get('name')
        artist = kwargs.get('artist')
        album = kwargs.get('album')

        if name is not None:
            return SongModel.objects.get(song_name = name)
        if artist is not None:
            return SongModel.objects.get(artist = artist)
        if album is not None:
            return SongModel.objects.get(album = album)
        return None

    def resolve_songs (self,info, **kwargs):
        return SongModel.objects.all()


schema = graphene.Schema(query= Query)
