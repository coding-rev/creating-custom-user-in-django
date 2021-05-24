# register/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):
	
	class Meta(UserCreationForm.Meta):
		model = Users
		list_display = ['email','companies_name', 'country']
		fields = UserCreationForm.Meta.fields + ('email', 'country', 'companies_name')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = Users
		fields = UserChangeForm.Meta.fields


