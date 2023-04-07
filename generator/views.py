from django.shortcuts import render
from django.http import HttpResponse
import random
import re

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = 10
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def discription(request):
    return render (request, 'generator/discription.html')
