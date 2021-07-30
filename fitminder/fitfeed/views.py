import json
import requests

from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect

from django import forms
from django.contrib.auth.decorators import login_required

from celery import shared_task

from .models import Reminder
from .forms import OneOffReminderForm, PeriodicTaskForm, ReminderForm

from django_celery_beat.models import PeriodicTask
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView

from fortune import utils
from fortune.models import Fortune, Pack


def load_fortunes():
	fortunes_path = utils.get_fortunes_path()
	art_fortunes_path = fortunes_path.joinpath("art")
	Pack.load(str(art_fortunes_path))



# MESSAGE BUILDER - Prepares reminder object, attaches Selected options (weather, joke)
def build_and_send_message(reminder):
	message = reminder.message

	print("------   SUCCESSFULLY BUILT MESSAGE  ------", message)

	# Check for User selection for Weather with location
	# Using Browser GeoIP - https://docs.djangoproject.com/en/1.11/ref/contrib/gis/geoip/
	if reminder.weather and reminder.latitude and reminder.longitude:
		try:
			weather_url = settings.WEATHER_API_BASE_URL.format(
				api_key=settings.WEATHER_API_KEY,
				coords=','.join([str(reminder.latitude), str(reminder.longitude)])
			)
			request = requests.get(weather_url)

			# Troubleshoots than weather requests other than ="200" 
			if request.status_code == 200:
				text = ('The weather today is ' + request.json()['current']['condition']['text']) + ' ' 
				temperature = ('and ' + str(request.json()['current']['temp_c'])) +  ' degrees Celcius. '

				prefix = text + temperature
				message = prefix + message
				print(message)
		except Exception as e:
			print(e)

	if reminder.joke:
		load_fortunes()
		message = message + '. And now a joke: ' + Fortune.fortune()
		print(message)
	# Try to connect to RaspberryPI server
	# Attatch message as description
	try:
		request = requests.get('http://192.168.1.74:8080', params={
			'thisPT_description': message
		})
	except Exception as e:
		print(e)


@shared_task()
def mainTask(pk):
	reminder = Reminder.objects.get(pk=pk)
	build_and_send_message(reminder)



@shared_task()
def one_off_task(form_data):
	reminder = Reminder(**form_data)
	build_and_send_message(reminder)


class ReminderListView(ListView):
	model = Reminder
	template_name = "fitfeed/index.html"
	# Django middleware processes user is_logged in...
	def get_queryset(self):
		if self.request.user.is_anonymous:
			return self.model.objects.none()
		# Show the reminders that are owned by the current user
		return self.model.objects.filter(author=self.request.user)

class ReminderEditView(UpdateView):
	model = Reminder
	form_class = ReminderForm

	# Form to edit reminder objects
	def form_valid(self, form):
		self.object = form.save()
		schedule = form.cleaned_data.get('schedule')
		if schedule:
			# User has prompted us to change the task schedule - let's edit that
			task = self.object.task
			task.interval = schedule
			task.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('reminder-edit', kwargs={'pk': self.object.pk})


class ReminderCreateView(CreateView):

	model = PeriodicTask
	form_class = PeriodicTaskForm
	initial = {'task': 'fitfeed.views.mainTask'}

	# Provides form and hides preset TASK name
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['task'].widget = forms.HiddenInput()
		# form.fields['start_time'].widget = forms.DateTimeInput()
		# form.fields['expires'].widget = forms.DateTimeInput()
		return form

	# Get, Check and return Periodictask form details
	def form_valid(self, form):


		self.object = PeriodicTask(name=form.cleaned_data['name'], 
			task=form.cleaned_data['task'],
			interval=form.cleaned_data['interval'],
			start_time=form.cleaned_data['start_time'],
			expires=form.cleaned_data['expires'],
			)

		self.object.save()
		print(self.object.start_time)
		reminder = Reminder.objects.create(
			task=self.object,
			message=form.cleaned_data['name'],
			author=self.request.user,
			joke=form.cleaned_data['joke'],
			weather=form.cleaned_data['weather'],
			latitude=form.cleaned_data['latitude'],
			longitude=form.cleaned_data['longitude'],
		)
		self.object.kwargs = json.dumps({"pk": reminder.pk})
		self.object.save()
		return redirect('index')

	# Redirect to submitted task in form
	def get_success_url(self):
		# One to One Relationship of REMINDER and PERIODICTASK
		# so this should be fine
		return reverse('reminder-edit', kwargs={'pk': self.object.reminder_set.first().pk})


class OneOffReminderView(FormView):
	form_class = OneOffReminderForm

	template_name = "fitfeed/reminder_form_one_off.html"

	def form_valid(self, form):
		#Form is directly passed to a Celery
		one_off_task.delay(form.cleaned_data)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('index')


class DeleteReminderView(DeleteView):
	model = Reminder

	def delete(self, request, *args, **kwargs):
		reminder = self.get_object()
		reminder.task.delete()
		return redirect('index')
		