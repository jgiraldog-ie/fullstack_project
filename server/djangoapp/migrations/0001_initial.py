# Generated by Django 5.1 on 2024-08-10 05:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=50)),
                (
                    'type',
                    models.CharField(
                        choices=[
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
                            ('COMPACT', 'Compact Car')
                        ],
                        default='SUV',
                        max_length=12
                    )
                ),
                (
                    'year',
                    models.IntegerField(
                        default=2023,
                        validators=[
                            django.core.validators.MaxValueValidator(2023),
                            django.core.validators.MinValueValidator(2015)
                        ]
                    )
                ),
                (
                    'transmission',
                    models.CharField(
                        choices=[
                            ('MANUAL', 'Manual'),
                            ('AUTOMATIC', 'Automatic'),
                            ('CVT', 'Continuously Variable Transmission')
                        ],
                        default='AUTOMATIC',
                        max_length=10
                    )
                ),
                (
                    'car_make',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='djangoapp.carmake'
                    )
                ),
            ],
        ),
    ]
