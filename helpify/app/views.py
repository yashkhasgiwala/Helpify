from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm, ReportForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import HUser, Report
from django.views.generic import CreateView
from classifier import Classifier
import requests
import json
from twilio.rest import Client

account_sid = 'AC00088dd46fa24adfe1ea7286f2d57324'
auth_token = '48695f9b9546c1035105d574b3b2b4e1'

client = Client(account_sid, auth_token)

classify = Classifier()

def register(response):
	if response.user.is_authenticated:
		return redirect("/")

	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			new_user = form.save()
			messages.info(response, "Thanks for registering. You are now logged in.")
			new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
			login(response, new_user)
			return redirect("/")
	else:
		form = RegisterForm()
	return render(response, "app/register.html", {"form":form})


def faq(response):
	return render(response, "app/faq.html")		

def home(response):
    return render(response, "app/home.html") 

@login_required(login_url='/login/')
def view_profile(request):
    return render(request, "app/profile.html", {'user': request.user})

@login_required(login_url='/login/')
def edit_profile(request):
	if request.user.has_usable_password():
		if request.method == 'POST':
			form = EditProfileForm(request.POST, instance=request.user)

			if form.is_valid():
				form.save()
				messages.success(request, "Changes are saved.")
				return redirect('/profile')
		else:
			form = EditProfileForm(instance=request.user)
	else:
		messages.info(request, "You cannot edit your profile on this account.")
		return redirect("/profile")
	return render(request, "app/edit_profile.html", {'form': form})

def report(response):
    if response.method == 'POST':  # check post
        form = ReportForm(response.POST, response.FILES)
        if form.is_valid():
            data = Report()  # create relation with model
            data.reg_plate = form.cleaned_data['reg_plate']
            data.image = form.cleaned_data['image']
            data.ip = response.META.get('REMOTE_ADDR')
            #data.latitude = lat
            #data.longitude = lon
            
            data.save()  # save data to table
            output = classify.classify(data.image.url[1:])
            if output:
                registered = HUser.objects.filter(reg_plate1=data.reg_plate)
                print(registered)


                r = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=hospital&inputtype=textquery&locationbias=ipbias&fields=formatted_address,name,geometry,place_id&key=AIzaSyCBIRp6BtwWH4aUxMqnk5F1APhP5CU0QG8')
                hospital = r.json()['candidates'][0]
                print(hospital)
                r = requests.get('https://maps.googleapis.com/maps/api/place/details/json?place_id='+hospital['place_id']+'&fields=vicinity,name,geometry,place_id,formatted_phone_number,international_phone_number&key=AIzaSyCBIRp6BtwWH4aUxMqnk5F1APhP5CU0QG8')
                details = json.loads(r.content)
                print(details['result'])
                messages.success(response, "Thanks for you help. We have contacted the local authorities.")


                if registered:
                    contact = registered.values('contact_phone1')[0]
                    print(contact['contact_phone1'])
                    name = registered.values('first_name')[0]
                    body = name['first_name']+' has been in an accident. Please go to '+ details['result']['name'] +', '+ details['result']['vicinity'] +' to visit them'

                    message = client.messages.create( 
                              from_='+15089283923', 
                              body = body, 
                              to = contact['contact_phone1']
                          ) 
                    print(message.sid) 
                return render(response, "app/hospitals.html", {'report' : data, 'hospital': details['result']})
            else:
                data.delete()
                messages.warning(response, "Fake images are not allowed.")
            return render(response, "app/report.html", {'form': form})
    else:
    	form = ReportForm()

    return render(response, "app/report.html", {'form': form})