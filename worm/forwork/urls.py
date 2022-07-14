from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('Roles', views.Roles, name='Roles'),
    path('createRole', views.createRole, name = 'CreateR'),
    path('createUsers', views.createUsers, name ='CreateUsers'),
    path('<int:pk>', views.DetailStaf.as_view(), name ='detailStaf'),
    path('<int:pk>/update', views.StafUpdate.as_view(), name ='updateStaf'),
    path('<int:pk>/updatet', views.RoleUpdate.as_view(), name ='updateRole')
]