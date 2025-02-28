from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows destinations to be viewed or edited.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
