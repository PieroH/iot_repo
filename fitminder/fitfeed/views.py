
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request

def home(request):
    return render(request, 'fitfeed/home.html')

@login_required
def feed(request):
    return render(request, 'fitfeed/feed.html')
