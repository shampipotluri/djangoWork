from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def home(requests):
    return HttpResponse('This is home page')

def aboutme(requests):
    return HttpResponse('I am Shampi')

def hobbies(requests):
    return HttpResponse('I love writing, reading and travelling')

