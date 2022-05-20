from django.urls import path
from .views import inicio, login_request, register_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',inicio,name='inicio'),
    path('login/',login_request,name='login'),
    path('logout/',LogoutView.as_view(template_name='inicio/logout.html'),name='logout'),
    path('singup/',register_view,name="singup")
]
