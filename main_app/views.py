from django.shortcuts import render
from django.views.generic.edit import CreateView

# models
class Wish:
    def __init__(self, description):
        self.description = description

wishes = [
    Wish('Colt45'),
    Wish('2 Zigzags'),
]




# Create your views here.
class WishCreate(CreateView):
  model = Wish
  fields = '__all__'


# Define the home view
def home(request):
  return render(request, 'home.html', {'wishes': wishes})

def add(request):
  return render(request, 'add.html', )