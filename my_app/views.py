from django.shortcuts import render

# views.py

class Plant:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

# Create a list of Plant instances
plants = [
    Plant('Aloe', 'aloe vera', 'Low maintenance succulent.', 3),
    Plant('Fern', 'boston fern', 'Loves humidity.', 0),
    Plant('Rose', 'rose', 'Beautiful flowering plant.', 4),
    Plant('Bamboo', 'lucky bamboo', 'Grows quickly indoors.', 6)
]

# Create your views here.
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plant_index(request):
    return render(request, 'plants/index.html', {'plants': plants})

