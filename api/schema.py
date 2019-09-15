from graphene_django import DjangoObjectType
from .models import SongModel
import graphene

class Song(DjangoObjectType):
    class Meta:
        model = SongModel

class Query(graphene.ObjectType):
    songs = graphene.List(Song)

    def resolve_songs (self,info):
        return SongModel.objects.all()


schema = graphene.Schema(query= Query)
