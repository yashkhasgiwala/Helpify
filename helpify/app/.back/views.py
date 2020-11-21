from django.shortcuts import render, redirect
from .models import HUser as User
from .forms import RegisterForm, EditProfileForm

from cuser.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def frontend(request):
	login_form = AuthenticationForm()
	register_form = RegisterForm()
	"""Vue.js will take care of everything else."""

	return render(request, 'app/template.html', {'login_form' : login_form, "register_form":register_form})


def login_user(response):
	if response.method == "POST":
		login_form = AuthenticationForm(response.POST)
		if login_form.is_valid():
			user = authenticate(username=login_form.cleaned_data['email'],
                                    password=login_form.cleaned_data['password'],
                                    )
			login(response, user)
			return redirect("/")
	else:
		login_form = AuthenticationForm()

	return render(response, 'app/template.html', {'login_form' : login_form})

def logout_user(response):
	if response.user.is_authenticated:
		logout(response)

	return redirect("/")

def register(response):
	if response.user.is_authenticated:
		return redirect("/")
	if response.method == "POST":
		register_form = RegisterForm(response.POST)
		if register_form.is_valid():
			new_user = register_form.save()
			new_user = authenticate(username=register_form.cleaned_data['username'],
                                    password=register_form.cleaned_data['password1'],
                                    )
			login(response, new_user)
			return redirect("/")
	else:
		register_form = RegisterForm()
	return render(response, "app/template.html", {"register_form":register_form})