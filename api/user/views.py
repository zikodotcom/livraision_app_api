from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .Serializer import UserSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_list_or_404
# Create your views here.

# TODO Views for admin
@api_view(['POST'])
def add_user_admin(request):
    data = request.data
    if 'password' in data:
        data['password'] = make_password(data['password'])
    data['type'] = 'admin'
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user_admin(request, pk):
    data = request.data
    items = User.objects.get(pk=pk)
    if 'password' in data:
        data['password'] = make_password(data['password'])
        items.password = data['password']
        items.save()
    serializer = UserSerializer(items)
    return Response(serializer.data)
    



# TODO Display list of client user


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_list_user(request):
    querySet = User.objects.exclude(type='admin')
    serializer = UserSerializer(querySet, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# TODO Activate or desactivate client
@api_view(['PUT'])
def activate_desactivate_client(request, pk):
    client = User.objects.get(pk=pk)
    if client:
        client.is_active = not client.is_active
        client.save()
        return Response({"message" "client activate by success"})
    else:
        return Response({"message": "client activate by success"} , status=status.HTTP_404_NOT_FOUND)