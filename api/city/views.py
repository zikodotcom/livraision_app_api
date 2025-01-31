from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .seializer import CitySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import City
from .Pagination import CityPagination
# Create your views here.

# TODO Get list of all city or filter by one city
@api_view(['GET'])
def get_citys(request):
    params = request.query_params
    querySet = ''
    if 'zone' in params:
        querySet = City.objects.filter(zone=params['zone'])
        serializer = CitySerializer(querySet, many=True)
    else:
        paginator = CityPagination()
        querySet = City.objects.prefetch_related('zone').all()
        paginate_data_queryset = paginator.paginate_queryset(querySet, request, view=False)
        serializer = CitySerializer(paginate_data_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

# TODO Create city

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def add_city(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = CitySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# TODO Update city
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_city(request, pk):
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response({'error' : 'City not found'}, status=status.HTTP_404_NOT_FOUND)
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = CitySerializer(city,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# TODO DELETE city
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_city(request, pk):
    city = City.objects.get(pk=pk)
    city.delete()
    return Response({'message': 'Ville supprimer avec success'}, status=status.HTTP_200_OK)



