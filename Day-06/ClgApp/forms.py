from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from ClgApp.models import User
from django import forms

class RgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["usrole","roll","username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		"roll":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Roll Number",
			}),
		"usrole":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Userup(ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2"
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Emailid",
			}),
		}

class UsrgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}





