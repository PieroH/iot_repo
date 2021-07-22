# import json
# import requests
import calendar
import datetime

from django.shortcuts import render
from django.http import request
from .models import Event

from calendar import HTMLCalendar
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView
from django.db import models
from django.contrib.auth.models import User


def feed(request):
	context = {
		'events': Event.objects.all()	
	}
	return render(request, 'fitfeed/feed.html', context)


class EventListView(ListView):
	model = Event
	template_name = 'fitfeed/base.html' # <app> /<model>_<viewtype>.html
	context_object_name = 'event'
	# queryset = Event.objects.order_by('start_date')
	ordering = ['-date_published']


class EventDetailView(DetailView):
	model = Event

	def event_detail(request, pk):
		context = {
			'events': Event.objects.filter(pk=pk)
		}
		return render(request, 'event-detail.html', context)


class EventCreateView(LoginRequiredMixin, CreateView):
	model = Event

	fields = [
		'event_name', 
		'start_date',
		'start_time',
		'end_date',
		'end_time',
		'description',
		'location',
	]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)





def home(request):
	# month = month.capitalize()
	# m = list(calendar.month_name)

	# for i in range(1, len(m)):
	# 	month_number[i] = m[i]

	# # now = datetime.now()
	# # current_year = now.year

	# cal = calendar.HTMLCalendar(firstweekday = 0)
	# cal = cal.formatmonth(year, month_number)

	# time = now.strftime('%I:%M:%S %p')

	# context = {
	# 	"year" : year,
	# 	"month" : month,
	# 	"month_number" : month_number,
	# 	"current_year" : current_year,
	# 	"cal" : cal,
	# 	# "time" : time
	# }

	return render(request, 'fitfeed/home.html')


def feed(request):
	context = {}
	return render(request, 'fitfeed/feed.html', context)








# API_TOKEN = "ze4qFa7v"
# API_USR = "piotraexrx"

# AUTH_URL = "https://exrx.tk/consumer/login"
# QUERY_URL = "http://204.235.60.194/exrxapi/v1/allinclusive/exercises?exercisename={}"

# I suggest you use this library: https://docs.python-requests.org/en/master/
# You should use pip to install it in the environment where your Django app needs to run
# Then, as part of one of your Views - the part of the Django app where all the business logic lives -
# you can import the library and use it to get the data you need. Bear in mind that requests made in this way to
# the API will be made synchronously and will block the view until they either time out or have returned a response

# @login_required
# def feed(request):

# 	query = request["burpee"]

# 	payload = {"username": API_USR, "password": API_TOKEN}

# 	token = requests.post(AUTH_URL, data=payload).json()["token"]

# 	auth_headers = {"Autorization": "Bearer {}".format(token)}

# 	api_data = requests.get(QUERY_URL.format(query), headers=auth_headers)

# 	context = {
# 		api_data.json()
# 	}

# 	return render(request, 'fitfeed/home.html', context)


"""
Assumed workflow: user submits a GET request to the application with a query term. 
The application uses the query term to retrieve data from the API and returns it to the user.
"""