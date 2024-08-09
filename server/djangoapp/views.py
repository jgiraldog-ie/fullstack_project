# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime
from .models import CarMake, CarModel

from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)

def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if(count == 0):
        initiate()
    cars = []
    car_models = CarModel.objects.all()  # O ajusta el queryset según sea necesario

    for car_model in car_models:
        cars.append({
            "CarModel": {
                "name": car_model.name,
                "type": car_model.type,
                "year": car_model.year,
                "transmission": car_model.transmission,
                "car_make": {
                    "name": car_model.car_make.name,
                    "description": car_model.car_make.description,
                    "country": car_model.car_make.country
                }
            }
        })
    
    return JsonResponse({"CarModels": cars})

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    username = request.user.username
    logout(request)
    data = {"userName": username}
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        
        if not all([username, password, first_name, last_name, email]):
            return HttpResponseBadRequest("Missing fields.")

        # Check if username or email already exists
        username_exists = User.objects.filter(username=username).exists()
        email_exists = User.objects.filter(email=email).exists()

        if username_exists or email_exists:
            data = {"userName": username, "error": "Username or Email already registered"}
            return JsonResponse(data)

        # Create user
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            data = {"userName": username, "status": "Authenticated"}
            return JsonResponse(data)
        else:
            return HttpResponseBadRequest("Authentication failed after registration.")

    return HttpResponseBadRequest("Invalid request method.")

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
