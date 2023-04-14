from django.urls import path
from . import views

urlpatterns = [
    path('suma/', views.Calculadora.suma),
    path('resta/', views.Calculadora.resta),
    path('multiplicacion/', views.Calculadora.multiplicacion),
    path('division/', views.Calculadora.division),
]
