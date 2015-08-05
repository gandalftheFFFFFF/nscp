__author__ = 'niels'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class CreateUserForm(LoginForm):
    password_validation = forms.CharField(widget=forms.PasswordInput, label='Password again')


class UserProfileForm(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company'}))
