from django.urls import path
from . import views
urlpatterns = [
    path('create-zone', views.create_zone),
    path('list-zone', views.list_zone),
    path('update-zone/<uuid:pk>', views.update_zone),
    path('delete-zone/<uuid:pk>', views.delete_zone),
]