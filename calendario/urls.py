from django.urls import path
from .views import calendario, cadastroevento, fornecedores, cadastrofornecedor, atualizafornecedor, apagarfornecedor, clientes, cadastrocliente, apagarcliente, atualizacliente

urlpatterns = [
    path('', calendario, name='calendario'),
    path('cadastro/', cadastroevento, name='cadastroevento'),

    
    path('fornecedores/', fornecedores, name='fornecedores'),
    path('fornecedores/cadastro', cadastrofornecedor, name='cadastrofornecedor'),
    path('fornecedores/atualiza/<int:id>/', atualizafornecedor, name='atualizafornecedor'),
    path('fornecedores/apagar/<int:id>/', apagarfornecedor, name='apagarfornecedor'),


    path('clientes/', clientes, name='clientes'),
    path('clientes/cadastro', cadastrocliente, name='cadastrocliente'),
    path('clientes/atualiza/<int:id>/', atualizacliente, name='atualizacliente'),
    path('clientes/apagar/<int:id>/', apagarcliente, name='apagarcliente'),
]