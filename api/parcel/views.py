from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Parcel
# # Create your views here.


# # TODO Get parcel for admin

# @api_view('GET')
# @permission_classes([IsAdminUser, IsAuthenticated])
# def get_parcel_for_admin(request):
#     queryset = Parcel.
