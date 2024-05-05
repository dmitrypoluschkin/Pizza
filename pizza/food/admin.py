from django.contrib import admin
from .models import Pizza, Roll, Drink


# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(Pizza, PizzaAdmin)


class RollAdmin(admin.ModelAdmin):
    list_display = ('name', 'price5', 'price10')


admin.site.register(Roll, RollAdmin)


class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(Drink, DrinkAdmin)
