from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def food(requests):
    return HttpResponse('Travel and taste yummy food from different places')

def water(requests):
    return HttpResponse('Drink more water to stay healthy')
