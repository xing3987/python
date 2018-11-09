# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
    password2=forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
    
    class Meta:
        model=User
        fields=("username","email")
        
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('passwords do not match')
        return cd['password']
