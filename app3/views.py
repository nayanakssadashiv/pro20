from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index3(request,data):
    return HttpResponse(f'<h2>city name {data}</h2>')