from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    ctx = {'name': 'Western Pizza',}
    return render(request, 'food/index.html', ctx)


def pizza(request):
    return render(request, 'food/pizza.html')


def rolls(request):
    return render(request, 'food/rolls.html')


def drinks(request):
    return render(request, 'food/drinks.html')