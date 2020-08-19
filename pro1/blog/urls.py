from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from blog import views
urlpatterns=[
        url(r'food.*',views.food,name='food'),
        url(r'water.*',views.water,name='water'),
]
