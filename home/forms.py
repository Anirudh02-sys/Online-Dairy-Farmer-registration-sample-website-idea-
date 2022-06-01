from dataclasses import field
from django import forms
from .models import Farmer

'''
class FarmerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = Farmer
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }
        fields = ['fname', 'lname', 'email', 'phno', 'password']
'''


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['fname', 'lname', 'email', 'phno', 'password']


class LoginFarmer(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['email', 'password']
