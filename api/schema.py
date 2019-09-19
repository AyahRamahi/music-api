from graphene_django import DjangoObjectType
from .models import SongModel
import graphene

class Song(DjangoObjectType):
    class Meta:
        model = SongModel

class Query(graphene.ObjectType):
    song = graphene.List(graphene.String, album= graphene.String())
    all_songs = graphene.List(Song)

    artists = graphene.List(graphene.String)
    albums = graphene.List(graphene.String, artist=graphene.String())

    def resolve_albums(self, info, **kwargs):
        artist = kwargs.get('artist')

        if artist is not None:
            albums_query = SongModel.objects.filter(artist=artist).values('album').distinct()
            albums_list = []
            for album in albums_query:
                albums_list.append(album['album'])
            return albums_list
        return None

    def resolve_artists(self, info, **kwargs):
        artists_query = SongModel.objects.values('artist').distinct()
        artists_list = []
        for artist in artists_query :
            artists_list.append(artist['artist'])
        return artists_list

    def resolve_song (self, info, **kwargs):
        album = kwargs.get('album')

        if album is not None:
            songs_query = SongModel.objects.filter(album=album).values('song_name')
            songs_list = []
            for song in songs_query:
                songs_list.append(song['song_name'])
            return songs_list
        return None

    def resolve_all_songs (self,info, **kwargs):
        return SongModel.objects.all()


schema = graphene.Schema(query= Query)
