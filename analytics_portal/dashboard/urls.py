from django.urls import path
from . import views

urlpatterns = [
    path('tabla/', views.tabla, name='tabla'),
    path('', views.index, name='index'),
]