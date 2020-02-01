from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from crispy_forms.helper import FormHelper
from .forms import *

# Create your views here.
def home(request):
	return render(request, 'app/index.html')

def login(request):
	return render(request, 'users/loginn.html')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			return redirect('login')
	else:
		form = RegistrationForm()
	return render(request, 'app/register.html', {'form': form})





