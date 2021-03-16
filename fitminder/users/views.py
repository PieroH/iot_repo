from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from fitfeed.models import Feed
from users.models import FitProfile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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

@login_required
def profile(request):
	return render(request, 'users/profile.html')

	# context = {
	# 	'details': FitProfile.objects.filter(pk=pk)
	# }


# def profile(request):
# 	# UPDATING USER PROFILE BELOW - validation, POST and FIELD request
# 	if request.method == 'POST':
# 		user_form = UserUpdateForm(request.POST, instance=request.user)
# 		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.fitprofile)

# 		if user_form.is_valid() and profile_form.is_valid():
# 			user_form.save()
# 			profile_form.save()
# 			# some user feedback same as in UserRegistaraion
# 			messages.success(request, f'Account updated!')
# 			return redirect('profile')
# 	else:
# 		user_form = UserUpdateForm(instance=request.user)
# 		profile_form = ProfileUpdateForm(instance=request.user.fitprofile)

# 	context = {
# 		'user_form': user_form,
# 		'profile_form': profile_form,
# 	}
# 	return render(request, 'users/profile.html', context)