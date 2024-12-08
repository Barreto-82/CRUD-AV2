from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
    path('novo/', views.cria_produto, name='cria_produto'),
    path('<int:pk>/editar/', views.edita_produto, name='edita_produto'),
    path('<int:pk>/deletar/', views.deleta_produto, name='deleta_produto'),
]
