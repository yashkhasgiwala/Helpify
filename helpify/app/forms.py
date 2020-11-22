from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import HUser as User
from app.models import Report

class RegisterForm(UserCreationForm):
	
	class Meta:
		model = User
		labels = {
		"reg_plate1": "Enter your Vehicle Licence plate Number",
		"contact_phone1": "Emergency Contact Number" 
		}
		fields = ["first_name", "last_name", "email", "phone", "reg_plate1", "contact_phone1", "password1", "password2"]
        #"reg_plate1", "reg_plate2", "contact_phone1", "contact_phone2", "contact_phone3", 

class EditProfileForm(UserChangeForm):
	password = None
	current_password = forms.CharField(required=True, widget=forms.PasswordInput, label="Current password")

	class Meta:
		model = User
		fields = [ "email", "first_name", "last_name", "phone", "reg_plate1", "contact_phone1", "current_password"]

	def clean_current_password(self):
         valid = self.instance.check_password(self.cleaned_data['current_password'])
         if not valid:
             raise forms.ValidationError("Password is incorrect.")
         return valid

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        labels = {
        "image": "Upload a picture of the accident:",
        "reg_plate": "Enter the Licence plate Number: " 
    	}
        fields = ['image', 'reg_plate']