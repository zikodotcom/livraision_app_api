from django.urls import path
from . import views
urlpatterns = [
    path('admin/add_user', views.add_user_admin),
    path('admin/update_user/<int:pk>', views.update_user_admin),
    path('admin/list_user', views.get_list_user),
    path('admin/activate_desactivate_client/<int:pk>', views.activate_desactivate_client),

]