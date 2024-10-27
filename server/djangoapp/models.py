from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    founded_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(now().year)
        ],
        blank=True,
        null=True
    )
    # Add any other fields you deem necessary

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    HATCHBACK = 'Hatchback'
    MINIVAN = 'Minivan'
    TRUCK = 'Truck'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
        (HATCHBACK, 'Hatchback'),
        (MINIVAN, 'Minivan'),
        (TRUCK, 'Truck'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    # Add any other fields you deem necessary

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
