# mi_crud_app/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('lista_productos/', views.ListaProductosView.as_view(), name='lista_productos'),
    path('agregar_producto/', views.AgregarProductoView.as_view(), name='agregar_producto'),
    path('editar_producto/<int:pk>/', views.EditarProductoView.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.EliminarProductoView.as_view(), name='eliminar_producto'),
    path('detalle_producto/<int:pk>/', views.DetalleProductoView.as_view(), name='detalle_producto'),
     path('', views.home, name='home'),  # Esta URL coincide con la página de inicio
]

