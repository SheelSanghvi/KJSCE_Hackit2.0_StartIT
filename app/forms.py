from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from crispy_forms.helper import FormHelper

class RegistrationForm(ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=[ 'email', 'f_name', 'l_name', 'gender','age', 'phone', 'logo', 'password', 'confirm_password']
		
		labels = {
        "f_name": "first name",
        "l_name": "last name",
    	}
	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
			raise forms.ValidationError("Passwords don't match")

	
	# helper.layout = Layout(
	#             Field('email', placeholder='email'),
	#             Field('f_name', placeholder='first name'),
	#             Field('l_name', placeholder='last name'),
	#             FormActions(ButtonHolder(Submit('submit', 'Search', css_class='btn btn-primary')))
	#         )

	# helper.form_class = 'form-inline'
	# helper.field_template = 'bootstrap3/layout/inline_field.html'
	# helper.layout = Layout(
	#     'email',
	#     'f_name',
	#     'l_name',
	#     StrictButton('Sign in', css_class='btn-default'),
	# )