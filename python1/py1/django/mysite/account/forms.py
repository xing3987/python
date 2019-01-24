# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,UserInfo

class LoginForm(forms.Form):#form只能有实体定义的input框
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):  #ModelForm可以有除实体外的input
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
    password2=forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
    
    class Meta:
        model=User
        fields=("username","email")
        
    def clean_password2(self): #需要验证使用clean_函数
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('passwords do not match')
        return cd['password']
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=("birth","phone")
        
class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=("school","company","profession","address","aboutme","photo")
        
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("email",)
        
