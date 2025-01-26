from rest_framework import serializers
from zone.serializer import ZoneSerializer
from .models import City

class CitySerializer(serializers.ModelSerializer):
    zone_name = serializers.CharField(source='zone.zone_name', read_only=True)
    class Meta:
        model = City
        fields = "__all__"


