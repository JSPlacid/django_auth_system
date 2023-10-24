from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """
    form fields to overide inherited form fields
    """
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    # class meta:
    #     model = User
    #     fields = [
    #         'username',
    #         'email',
    #         'password1',
    #         'password2'
    #     ]
