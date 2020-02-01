from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from crispy_forms.helper import FormHelper
from .forms import *
from . import scrape
from . import seeds as newsScrape
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import json 
import ast 

# Create your views here.
final_list=[]
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
	

@login_required
def startup(request):
	final_list=scrape.GetInfo()
	news_list = newsScrape.getInfo()
	for i in final_list:
		try:
			Startup.objects.get(name=i['Name'])
		except Startup.DoesNotExist:
			Startup.objects.create(name=i['Name'], typee= i['Type'], logo=i['image'], stage=i['Stage'], location=i['Location'],  rating= i['Rating'])
			
	return render(request, 'app/startup.html', {'final': final_list,'news':news_list})


@login_required
def save(request):
	final_list=scrape.GetInfo()
	if request.method == "POST":
		y = request.POST['x']
		print(y)
		obj= Startup.objects.get(name=y)
		obj.user.add(request.user.id)
		obj.save()
	return render(request, 'app/startup.html', {'final': final_list})

@login_required
def watchLater(request):
	obj = Startup.objects.filter(user__id=request.user.id)
	print(obj)
	return render(request, 'app/watchLater.html', {'obj': obj})