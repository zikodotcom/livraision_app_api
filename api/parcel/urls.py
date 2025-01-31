from django.urls import path
from . import views


urlpatterns = [
    path('create_parcel', views.create_parcel),
    path('list_parcel_admin', views.get_parcel_for_admin),

]