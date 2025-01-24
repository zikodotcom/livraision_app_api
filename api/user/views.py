from django.shortcuts import render
from rest_framework.decorators import api_view
from .Serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


