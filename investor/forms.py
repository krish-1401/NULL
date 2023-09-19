from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'pan_number', 'email', 'phone_number','password1')
