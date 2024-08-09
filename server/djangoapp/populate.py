from .models import CarMake, CarModel
def initiate():
    car_make_data = [
    {"name": "NISSAN", "description": "Great cars. Japanese technology", "country": "Japan"},
    {"name": "Mercedes", "description": "Great cars. German technology", "country": "Germany"},
    {"name": "Audi", "description": "Great cars. German technology", "country": "Germany"},
    {"name": "Kia", "description": "Great cars. Korean technology", "country": "South Korea"},
    {"name": "Toyota", "description": "Great cars. Japanese technology", "country": "Japan"},
    {"name": "BMW", "description": "Great cars. German technology", "country": "Germany"},
    {"name": "Ford", "description": "Great cars. American technology", "country": "USA"},
]
    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description'], country=data['country']))

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "transmission": "AUTOMATIC"},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "transmission": "CVT"},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "transmission": "AUTOMATIC"},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "transmission": "AUTOMATIC"},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "transmission": "AUTOMATIC"},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "transmission": "CVT"},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "transmission": "AUTOMATIC"},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "transmission": "MANUAL"},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "transmission": "AUTOMATIC"},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "transmission": "AUTOMATIC"},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "transmission": "CVT"},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "transmission": "MANUAL"},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "transmission": "AUTOMATIC"},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "transmission": "CVT"},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4], "transmission": "AUTOMATIC"},
        {"name": "X7", "type": "SUV", "year": 2023, "car_make": car_make_instances[5], "transmission": "AUTOMATIC"},
        {"name": "Mustang", "type": "COUPE", "year": 2023, "car_make": car_make_instances[6], "transmission": "MANUAL"},
    ]

    for data in car_model_data:
            CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'], transmission=data['transmission'])