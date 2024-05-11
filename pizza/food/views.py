from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Pizza, Drink, Roll


# Create your views here.
def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)


def pizza(request):
    request.session.set_expiry(0)
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas,
           'active_link': 'pizza'}
    return render(request, 'food/pizza.html', ctx)


def rolls(request):
    request.session.set_expiry(0)
    rolls = Roll.objects.all()
    ctx = {'rolls': rolls,
           'active_link': 'rolls'}
    return render(request, 'food/rolls.html', ctx)


def drinks(request):
    request.session.set_expiry(0)
    drinks = Drink.objects.all()
    ctx = {'drinks': drinks,
           'active_link': 'drinks'}
    return render(request, 'food/drinks.html', ctx)


@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.method == 'POST' and request.is_ajax():
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        return JsonResponse({'success': True})
    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)


def success(request):
    return render(request, 'food/success.html')