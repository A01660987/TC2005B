from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fractions import Fraction
import json

class Calculadora:
    @csrf_exempt
    def suma(request):
        if request.method == "POST":
            data = json.loads(request.body)
            frac1 = Fraction(numerator=data['numerador1'], denominator=data['denominador1'])
            frac2 = Fraction(numerator=data['numerador2'], denominator=data['denominador2'])
            suma = frac1 + frac2
            resultado = {"num":suma.numerator, "den":suma.denominator}
            return JsonResponse(resultado)
        else:
            return HttpResponse("Error: Solo se aceptan requests por método POST.")
    
    @csrf_exempt
    def resta(request):
        if request.method == "POST":
            data = json.loads(request.body)
            frac1 = Fraction(numerator=data['numerador1'], denominator=data['denominador1'])
            frac2 = Fraction(numerator=data['numerador2'], denominator=data['denominador2'])
            resta = frac1 - frac2
            resultado = {"num":resta.numerator, "den":resta.denominator}
            return JsonResponse(resultado)
        else:
            return HttpResponse("Error: Solo se aceptan requests por método POST.")
    
    @csrf_exempt
    def multiplicacion(request):
        if request.method == "POST":
            data = json.loads(request.body)
            frac1 = Fraction(numerator=data['numerador1'], denominator=data['denominador1'])
            frac2 = Fraction(numerator=data['numerador2'], denominator=data['denominador2'])
            multiplicacion = frac1 * frac2
            resultado = {"num":multiplicacion.numerator, "den":multiplicacion.denominator}
            return JsonResponse(resultado)
        else:
            return HttpResponse("Error: Solo se aceptan requests por método POST.")
    
    @csrf_exempt
    def division(request):
        if request.method == "POST":
            data = json.loads(request.body)
            frac1 = Fraction(numerator=data['numerador1'], denominator=data['denominador1'])
            frac2 = Fraction(numerator=data['numerador2'], denominator=data['denominador2'])
            division = frac1 / frac2
            resultado = {"num":division.numerator, "den":division.denominator}
            return JsonResponse(resultado)
        else:
            return HttpResponse("Error: Solo se aceptan requests por método POST.")