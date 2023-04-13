from django.urls import path, include
from tabla import views

urlpatterns = [
    path('', views.index, name="index"),
    path('datos', views.datos, name="datos")
]