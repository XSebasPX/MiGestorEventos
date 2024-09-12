from django.urls import path
from . import views
from .views import OrganizadorListView, OrganizadorCreateView, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('crear/', views.crear_evento, name='crear_evento'),
    path('editar/<int:pk>/', views.editar_evento, name='editar_evento'),  
    path('eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),  
    path('organizadores/', OrganizadorListView.as_view(), name='lista_organizadores'),  
    path('organizadores/crear/', OrganizadorCreateView.as_view(), name='crear_organizador'),  
    path('organizadores/editar/<int:pk>/', views.editar_organizador, name='editar_organizador'),  
    path('organizadores/eliminar/<int:pk>/', views.eliminar_organizador, name='eliminar_organizador'),   
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),  
    path('dashboard/', dashboard, name='dashboard'),
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]