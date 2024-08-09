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
from .restapis import get_request, analyze_review_sentiments, post_review



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


def get_dealerships(request, state="All"):
    if(state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/"+state
    dealerships = get_request(endpoint)
    return JsonResponse({"status":200,"dealers":dealerships})

def get_dealer_details(request, dealer_id):
    if(dealer_id):
        endpoint = "/fetchDealer/"+str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status":200,"dealer":dealership})
    else:
        return JsonResponse({"status":400,"message":"Bad Request"})

def get_dealer_reviews(request, dealer_id):
    if(dealer_id):
        endpoint = "/fetchReviews/dealer/"+str(dealer_id)
        reviews = get_request(endpoint)
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])
            print(response)
            review_detail['sentiment'] = response['sentiment']
        return JsonResponse({"status":200,"reviews":reviews})
    else:
        return JsonResponse({"status":400,"message":"Bad Request"})

def add_review(request):
    if(request.user.is_anonymous == False):
        data = json.loads(request.body)
        try:
            response = post_review(data)
            return JsonResponse({"status":200})
        except:
            return JsonResponse({"status":401,"message":"Error in posting review"})
    else:
        return JsonResponse({"status":403,"message":"Unauthorized"})

