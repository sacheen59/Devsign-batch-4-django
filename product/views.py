from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# MVT => Model, View and Templates
# Model => data or databases
# Views => businesss logic
# Templates => html file or UI

# views => function based views and class based views
# function based views

def index(request):
    print("when url hits this function runs")
    return HttpResponse("This is index page")

def second_test(request):
    return HttpResponse("This is second test page.")
