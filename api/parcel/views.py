from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Parcel
from user.IsClient import IsClient
from .ParcelSerializer import ParcelSerializerForAdmin
from rest_framework.response import Response
from rest_framework import status
from city.models import City
from personalised_price.models import Personalised_price
# # Create your views here.


# # TODO Get parcel for admin

@api_view(['GET'])
@permission_classes([IsAdminUser, IsAuthenticated])
def get_parcel_for_admin(request):
    queryset = Parcel.objects.prefetch_related('user', 'city')
    serializer = ParcelSerializerForAdmin(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# TODO Add parcel for client
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsClient])
def create_parcel(request):
    data = request.data.copy()
    # TODO Check the price of colis in this city
    # TODO 1- Fetch the city and check if exists
    price = 0
    try:
        price_pers = Personalised_price.objects.get(city=request.data['city'], user=request.user.id)
        price = price_pers.new_price
    except Personalised_price.DoesNotExist:
        try:
            city = City.objects.get(pk=request.data['city'])
            price = city.price
        except City.DoesNotExist:
            return Response({'error': "Ville n'exist pas."})
    
    # TODO 3- Calcul the price
    data['price'] = (price * data['quantity'])
    data['user'] = request.user.id
    serializer = ParcelSerializerForAdmin(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
