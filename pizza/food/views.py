from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Drink, Roll


# Create your views here.
def index(request):
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)


def pizza(request):
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas,
           'active_link': 'pizza'}
    return render(request, 'food/pizza.html', ctx)


def rolls(request):
    rolls = Roll.objects.all()
    ctx = {'rolls': rolls,
           'active_link': 'rolls'}
    return render(request, 'food/rolls.html', ctx)


def drinks(request):
    drinks = Drink.objects.all()
    ctx = {'drinks': drinks,
           'active_link': 'drinks'}
    return render(request, 'food/drinks.html', ctx)