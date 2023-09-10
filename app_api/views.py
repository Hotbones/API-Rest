from rest_framework import viewsets
from .serializers import MoloSerializer
from .models import Molo

class MoloViewSet(viewsets.ModelViewSet):
    queryset=Molo.objects.all()
    serializer_class=MoloSerializer