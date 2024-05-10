from django import forms
from .models import Booking,Contact,Feedback
from django.forms import TextInput, EmailField, Select, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:  
        model = Booking  
        fields = ['name', 'email', 'phone', 'doctor', 'booked', 'time', 'desc']
        widgets = {
            "name": TextInput(attrs={
                "type": "text",
                "class": "form-control border-0",
                "placeholder": "Your Name",
                "style": "height: 55px;"
            }),
            "email": TextInput(attrs={
                "type": "email",
                "class": "form-control border-0",
                "placeholder": "Your email",
                "style": "height: 55px;"
            }),
            "phone": TextInput(attrs={
                "type": "text",
                "class": "form-control border-0",
                "placeholder": "Your phone",
                "style": "height: 55px;"
            }),
            "doctor": Select(attrs={
                "class": "form-control border-0",
                "style": "height: 55px; background-color:white"

            }),
           'booked':TextInput(attrs={
                "type":"date",
                "class":"form-control border-0",
                "style":"height: 55px;"
            }),
            "time": TextInput(attrs={
                "type": "time",
                "class": "form-control border-0",
                "style": "height: 55px;"
            }),
            "desc": Textarea(attrs={
                "type": "textarea",
                "class": "form-control border-0",
                "placeholder": "Describe your problem",
                "rows": "5"
            }),
        }

class UserRegistrationForm(UserCreationForm):
     username=forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control','placeholder':' Enter your  username'}))
     email=forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control','placeholder':' Enter your email '}))
     password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'forms-control','placeholder':' Enter your  password' }))
     password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'forms-control','placeholder':' Enter confirm password' })) 

class Meta:
        model = User
        fields = ['username','email','password1', 'password2']


# forms.py

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            "name": TextInput(attrs={
                "type": "text",
                "class": "form-control border-0",
                "placeholder": "Your Name",
                "style": "height: 55px;"
            }),
            "email": TextInput(attrs={
                "type": "email",
                "class": "form-control border-0",
                "placeholder": "Your email",
                "style": "height: 55px;"
            }),
            "subject": TextInput(attrs={
                "type": "text",
                "class": "form-control border-0",
                "placeholder": "Subject",
                "style": "height: 55px;"
            }),
            "message": Textarea(attrs={
                "class": "form-control border-0",
                "placeholder": "Your message",
                "style": "height: 150px;"  # Adjust height as needed
            }),
            # Add widgets for other fields as needed
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model= Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            "name": TextInput(attrs={
                "type": "text",
                "class": "form-control border-0",
                "placeholder": "Your Name",
                "style": "height: 55px;"
            }),
            "email": TextInput(attrs={
                "type": "email",
                "class": "form-control border-0",
                "placeholder": "Your email",
                "style": "height: 55px;"
            }),
            "message": Textarea(attrs={
                "class": "form-control border-0",
                "placeholder": "Your message",
                "style": "height: 150px;"  # Adjust height as needed
            }),
        }    