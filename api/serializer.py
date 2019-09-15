from rest_framework import serializers
from . import models

# serializer reads data from the model and converts it to json
class Serializer (serializers.ModelSerializer):
    # class Meta defines meta behavior of the serializer
    class Meta:
        # define the model for the serializer
        model = models.Song
        fields = ('album', 'artist', 'song_name')
