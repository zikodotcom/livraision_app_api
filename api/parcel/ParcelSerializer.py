from rest_framework import serializers
from .models import Parcel

class ParcelSerializerForAdmin(serializers.ModelSerializer):
    client_first_name = serializers.CharField(source='user.first_name', read_only=True) 
    client_last_name = serializers.CharField(source='user.last_name', read_only=True) 
    city_name = serializers.CharField(source='city.city_name', read_only=True) 
    class Meta:
        model = Parcel
        fields = '__all__'