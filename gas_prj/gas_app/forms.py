# gas_app/forms.py

from django import forms
from .models import Request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_type', 'description', 'file_attachment']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
