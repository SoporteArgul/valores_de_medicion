from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tiempo_de_carro', views.tiempo_de_carro,name='tiempo_de_carro'),
    path('control_de_descartes',views.control_de_descartes,name='control_de_descartes'),
    path('fin_op',views.fin_o_p,name='fin_op'),
    path('logout/',LogoutView.as_view(template_name='inicio/logout.html'),name='logout')]
    