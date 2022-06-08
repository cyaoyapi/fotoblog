"""
Module to define forms for app 'authentication'.
"""
from django import forms

class LoginForm(forms.Form):
    """
    Class to create login form.
    """
    username = forms.CharField(label="Nom utilisateur", max_length=100)
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput)