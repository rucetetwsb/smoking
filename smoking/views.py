from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Borough, SmokingArea, SmokingAreaType, Fine
from  django.views import generic

# Create your views here.
def boroughlist(request):
    return render(request, 'smoking/boroughlist.html')

def smokingmap(request):
    return render(request, 'smoking/map.html')

def location(request) :
    return render(request, 'smoking/location.html')

def cp_cd(request) :
    return render(request, 'smoking/cp_cd.html')

def graph(request) :
    return render(request, 'smoking/graph.html')

def direction(request) :
    return render(request, 'smoking/direction.html')

def songpa_map(request) :
    return render(request, 'smoking/songpa_map.html')