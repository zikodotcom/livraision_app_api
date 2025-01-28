from django.urls import path
from . import views
urlpatterns = [
    path('create-reclamation', views.create_reclamation),
    path('list-reclamation-admin', views.list_reclamation_for_admin),
    path('list-reclamation-client', views.list_reclamation_for_client),
    path('update-reclamation/<uuid:pk>', views.update_reclamation),
    path('delete-reclamation/<uuid:pk>', views.delete_reclamation),
]