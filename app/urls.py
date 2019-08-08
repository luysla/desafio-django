from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo_candidato', views.novo_candidato, name='novo_candidato'),
]