from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializer import ZoneSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Zone
# Create your views here.

# TODO List zone

@api_view(['GET'])
@permission_classes([IsAdminUser, IsAuthenticated])
def list_zone(request):
    querySet = Zone.objects.all()
    serializer = ZoneSerializer(querySet, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# TODO Create zone

@api_view(['POST'])
def create_zone(request):
    serializer = ZoneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Update zone

@api_view(['PUT'])
def update_zone(request, pk):
    queryset = Zone.objects.get(pk=pk)
    serializer = ZoneSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# TODO Delete zone

@api_view(['DELETE'])
def delete_zone(request, pk):
    queryset = Zone.objects.get(pk=pk)
    queryset.delete()
    return Response(status=status.HTTP_201_CREATED)