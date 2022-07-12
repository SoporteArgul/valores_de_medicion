from django.contrib import admin
from .models import control_de_descartes, fin_de_op, tiempo_de_carro

admin.site.register(tiempo_de_carro)
admin.site.register(control_de_descartes)
admin.site.register(fin_de_op)