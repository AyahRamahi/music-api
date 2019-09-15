from rest_framework import viewsets
from . import models
from . import serializer

# Create your views here.

# viewsets include logic to handle rest requests, and are used to
# solve the problem of boilerplate code in the views
class IndexViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.Serializer
    queryset = models.Song.objects.all()
