from django.shortcuts import render

# Create your views here.

def home(reqoest):
    return (reqoest, 'home.html')