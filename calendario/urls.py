from django.urls import path
from .views import calendario, fornecedores, cadastrofornecedores, clientes, cadastrocliente, cadastroevento

urlpatterns = [
    path('', calendario, name='calendario'),
    path('cadastro/', cadastroevento, name='cadastroevento'),

    
    path('fornecedores/', fornecedores, name='fornecedores'),
    path('fornecedores/cadastro', cadastrofornecedores, name='cadastrofornecedores'),


    path('clientes/', clientes, name='clientes'),
    path('clientes/cadastro', cadastrocliente, name='cadastrocliente'),
]