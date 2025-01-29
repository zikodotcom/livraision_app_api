from django.shortcuts import render
from .serializer import ReclamationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from user.IsClient import IsClient
from .models import Reclamation
# Create your views here.

# TODO List reclamation for admin

@api_view(['GET'])
@permission_classes([IsAdminUser, IsAuthenticated])
def list_reclamation_for_admin(request):
    querySet = Reclamation.objects.all()
    serializer = ReclamationSerializer(querySet, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# TODO List reclamation for client

@api_view(['GET'])
@permission_classes([IsClient,IsAuthenticated])

def list_reclamation_for_client(request):
    querySet = Reclamation.objects.filter(pk=request.user.id)
    serializer = ReclamationSerializer(querySet, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# TODO CREATE RECLAMATION
@api_view(['POST'])
@permission_classes([IsClient,IsAuthenticated])
def create_reclamation(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = ReclamationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO UPDATE RECLAMATION
@api_view(['PUT'])
@permission_classes([IsClient,IsAuthenticated])
def update_reclamation(request, pk):
    queryset = Reclamation.objects.get(pk=pk)
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = ReclamationSerializer(queryset, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete reclamation

@api_view(['DELETE'])
@permission_classes([IsClient,IsAuthenticated])
def delete_reclamation(request, pk):
    queryset = Reclamation.objects.get(pk=pk)
    queryset.delete()
    return Response(status=status.HTTP_201_CREATED)