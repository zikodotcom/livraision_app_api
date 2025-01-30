from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Parcel
from user.IsClient import IsClient
from .ParcelSerializer import ParcelSerializer
from rest_framework.response import Response
from rest_framework import status
# # Create your views here.


# # TODO Get parcel for admin

# @api_view('GET')
# @permission_classes([IsAdminUser, IsAuthenticated])
# def get_parcel_for_admin(request):
#     queryset = Parcel.objects.all()


# TODO Add parcel for client
@api_view(['POST'])
@permission_classes([IsAuthenticated,IsClient])
def create_parcel(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = ParcelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
