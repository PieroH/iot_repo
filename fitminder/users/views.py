from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from fitfeed.models import Feed
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created! You can Login now!')
			return redirect('feed-home')
	else:
		form = UserRegisterForm()
		messages.error(request, f'Something went wrong, try again!')
	# passing in form as context - ditionary of {variable form: newely created form UserCreationForm()}
	return render(request, 'users/register.html', {'form': form})

