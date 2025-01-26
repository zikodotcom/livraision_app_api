from django.urls import path
from . import views

urlpatterns = [
    path('create-city', views.add_city),
    path('update-city/<uuid:pk>', views.update_city),
    path('list-city/', views.get_citys),
    path('delete-city/<uuid:pk>', views.delete_city),
]