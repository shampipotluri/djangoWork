from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def home(requests):
    return render(requests,'vowels/home.html')

def result(requests):
    mytext=requests.GET['fulltext']
    #now, count the vowels in mytext. also remove the vowels and find the string
    resString=''
    vowelsCountA=0
    vowelsCountE=0
    vowelsCountI=0
    vowelsCountO=0
    vowelsCountU=0
    for x in mytext:
        if x=='a' or x=='A':
            vowelsCountA=vowelsCountA+1
        elif x=='e' or x=='E':
            vowelsCountE=vowelsCountE+1
        elif x=='i' or x=='I':
            vowelsCountI=vowelsCountI+1
        elif x=='o' or x=='O':
            vowelsCountO=vowelsCountO+1
        elif x=='u' or x=='U':
            vowelsCountU=vowelsCountU+1
        else:
            resString=resString+x
    return render(requests,'vowels/result.html',{'resString':resString,'vowelsCountA':vowelsCountA,'vowelsCountE':vowelsCountE,'vowelsCountI':vowelsCountI,'vowelsCountO':vowelsCountO,'vowelsCountU':vowelsCountU})

