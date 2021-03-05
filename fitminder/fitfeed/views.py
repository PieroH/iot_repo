
from django.shortcuts import render
from django.http import HttpResponse, request

def home(request):
    return render(request, 'fitfeed/home.html')


def feed(request):
    return render(request, 'fitfeed/feed.html')
