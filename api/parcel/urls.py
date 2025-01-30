from django.urls import path
from . import views


urlpatterns = [
    path('create_parcel', views.create_parcel)
]