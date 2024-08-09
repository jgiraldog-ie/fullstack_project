from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    CAR_TYPES = [
    ('SEDAN', 'Sedan'),
    ('COUPE', 'Coupe'),
    ('HATCHBACK', 'Hatchback'),
    ('SUV', 'SUV'),
    ('CROSSOVER', 'Crossover'),
    ('CONVERTIBLE', 'Convertible'),
    ('WAGON', 'Wagon'),
    ('PICKUP', 'Pickup Truck'),
    ('MINIVAN', 'Minivan'),
    ('SPORTS_CAR', 'Sports Car'),
    ('LUXURY_CAR', 'Luxury Car'),
    ('ELECTRIC', 'Electric Vehicle'),
    ('HYBRID', 'Hybrid Vehicle'),
    ('COMPACT', 'Compact Car'),
    ]
    type = models.CharField(max_length=12, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    
    TRANSMISSION_TYPES = [
    ('MANUAL', 'Manual'),
    ('AUTOMATIC', 'Automatic'),
    ('CVT', 'Continuously Variable Transmission'),
    ]
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_TYPES, default='AUTOMATIC')

    def __str__(self):
        return self.name