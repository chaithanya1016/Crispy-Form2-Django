from tkinter import Widget
from django import forms
from django import forms
from .models import Candidate
from django.core.validators import RegexValidator

class SignupForm(forms.ModelForm):

    #Validators
    first_name = forms.CharField(
        label='First Name', 
        min_length=4, 
        max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9\s]*$', message="Only Letters and Numbers are Allowed !")], 
        required=True,
        widget=forms.TextInput(attrs={'placeholder' : 'First Name'})
        )
    last_name = forms.CharField(
        label='Last Name', 
        min_length=4, 
        max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9\s]*$', message="Only Letters and Numbers are Allowed !")], 
        required=True,
        widget=forms.TextInput(attrs={'placeholder' : 'Last Name'})
        )
    email = forms.CharField(
        label='Email', 
        min_length=10, 
        max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="Special Characters are not Allowed !")], 
        widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Email Address'})
        )
    #Method 1
    #age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))

    #Method 2
    age = forms.CharField(
        label='Age', 
        min_length=1, 
        max_length=2, 
        validators=[RegexValidator(r'^[0-9]*$', message="Letters and Special Characters are not Allowed !")], 
        widget=forms.TextInput(attrs={'placeholder' : 'Enter Your Age'})
        )
    message = forms.CharField(
        label='About You', min_length=10, max_length=1000, 
        widget=forms.TextInput(attrs={
            'placeholder' : 'Talk a little about you',
            "rows":5, 
            })
        )

    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name','age', 'email', 'phone','message']

        #Outside Widget
        widgets = {
            'phone' : forms.TextInput(attrs = {
                    'style' : 'font-size: 13px',
                    'placeholder' : 'Phone',
                    'data-mask' : '(+00) 00000-00000'
                }
            )
        }


