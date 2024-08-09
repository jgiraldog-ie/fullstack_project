from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year', 'transmission', 'car_make')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year', 'transmission', 'car_make')
    ordering = ('-year',)

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name','description', 'country')
    search_fields = ('name',)
    list_filter = ('country',)

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)