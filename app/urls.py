from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_candidatos, name='crud_candidatos'),
]