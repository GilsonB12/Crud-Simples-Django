from django.urls import path
from app_crud import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('crud/homepage.html', views.pessoas, name='listagem_nomes'),
    path('delete/<int:id_pessoa>/', views.delete, name='delete_pessoa'),
    path('update/<int:id_pessoa>/', views.atualizar_pessoa, name='atualizar_pessoa')
]
