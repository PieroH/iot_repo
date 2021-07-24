from django import forms
from .models import Reminder
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class OneOffReminderForm(forms.Form):
	message = forms.CharField()
	joke = forms.BooleanField(required=False)
	weather = forms.BooleanField(required=False)
	latitude = forms.DecimalField(required=False)
	longitude = forms.DecimalField(required=False)



class ReminderForm(forms.ModelForm):
	class Meta:
		model = Reminder

		fields = [
			'message',
			'joke',
			'weather',
			'latitude',
			'longitude',
		]

	latitude = forms.DecimalField(required=False)
	longitude = forms.DecimalField(required=False)

	def __init__(self, *args, **kwargs):
		super(ReminderForm, self).__init__(*args, **kwargs)
		instance = kwargs.pop('instance', '')
		self.fields['schedule'] = forms.ModelChoiceField(queryset=IntervalSchedule.objects.all(), initial=instance.task.interval)


class PeriodicTaskForm(forms.ModelForm):
	class Meta:
		model = PeriodicTask
		labels = {
            'name': ('Message'),
        }
		fields = [
			'name',
			'task',
			'interval',
			'joke',
			'weather',
			'latitude',
			'longitude',
		]

	# Datetime picker reference:
    # https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html

	start_time = forms.DateTimeField(
	        input_formats=['%Y/%m/%d %H:%M'],
	        widget=forms.DateTimeInput(attrs={
	            'class': 'form-control datetimepicker-input',
	            'data-target': '#datetimepicker1'
	        })
	    )
	expires = forms.DateTimeField(
	        input_formats=['%Y/%m/%d %H:%M'],
	        widget=forms.DateTimeInput(attrs={
	            'class': 'form-control datetimepicker-input',
	            'data-target': '#datetimepicker2'
	        })
	    )

	joke = forms.BooleanField(required=False)
	weather = forms.BooleanField(required=False)
	latitude = forms.DecimalField(required=False)
	longitude = forms.DecimalField(required=False)
