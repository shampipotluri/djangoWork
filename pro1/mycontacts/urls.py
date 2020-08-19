from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mycontacts import views
urlpatterns=[
        url(r'friends.*',views.friends,name='friends'),
        url(r'family.*',views.family,name='family'),
]
