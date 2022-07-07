from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar_lentes, name='cargar_lentes'),
    path('search/', views.mostrar_lentes, name='mostrar_lentes'),
    path('update/<int:pk>', views.actualizar_lentes, name='actualizar_lentes'),
    path('delete/<int:pk>', views.eliminar_lentes, name='eliminar_lentes'),
]