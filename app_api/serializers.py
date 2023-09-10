from rest_framework import serializers
from .models import Molo

class MoloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Molo
        fields=fields = '__all__'