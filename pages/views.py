from django.shortcuts import render,redirect


from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib import messages


from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .decorators import *


# Create your views here.

#view to login the user who are already registered or use google login
#decorator to avoid this page after login
@unauthenticated_user
def login(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username = username,password = password)

		if user is not None:
			auth_login(request, user)
			return redirect('home')
		else:
			messages.info(request,'Username or Password incorrect')


	context = {}
	return render(request,'pages/login.html',context)




#view to create an account for user or redirects to login page
#decorator to avoid this page after login
@unauthenticated_user
def register(request):

	form = CreateUserForm()
	if request.method =='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			

			messages.success(request,'Account was successfully created for  '+ str(user))
			return redirect('login')
	context = {'form':form,}
	return render(request,'pages/register.html',context)	


def logout(request):

	auth_logout(request)
	return redirect('login')	


#simple home page with a decorator added to access only after login

@login_required(login_url='login')
def home(request):
	all_data = Data.objects.all
	context = {'all_data':all_data,}
	return render(request,'pages/home.html',context)	


@login_required(login_url='login')
def addcity(request):
	form = CityForm()
	if request.method =='POST':
		form = CityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form':form,}		
	return render(request,'pages/cityform.html',context)


#Using ajax to load the states, districts,cities simultaneously



@login_required(login_url='login')
def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    
    print("loading states")
    context = {
    'states': states,
    }
    return render(request, 'pages/state_dropdown.html', context)



@login_required(login_url='login')
def load_districts(request):
    state_id = request.GET.get('state')
    districts = District.objects.filter(state_id=state_id).order_by('name')
    context = {
    'districts': districts,
    }
    return render(request, 'pages/district_dropdown.html', context)



@login_required(login_url='login')
def load_cities(request):
    district_id = request.GET.get('district')
    cities = City.objects.filter(district_id=district_id).order_by('name')
    context = {
    'cities': cities,
    }
    return render(request, 'pages/city_dropdown.html', context)



