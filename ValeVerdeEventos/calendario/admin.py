from django.contrib import admin

# Register your models here.

from calendario.models import clientes, eventos, fornecedores

admin.site.register(clientes.t_cliente),
admin.site.register(eventos.t_evento),
admin.site.register(fornecedores.t_fornecedor),
