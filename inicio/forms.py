from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
  
class UserRegistrationForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required') 
    password1=forms.CharField(widget=forms.PasswordInput) 
    password1=forms.CharField(widget=forms.PasswordInput) 
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    class Meta:  
        model = User  
        fields = ('first_name','last_name','email','username', 'password1','password2')  