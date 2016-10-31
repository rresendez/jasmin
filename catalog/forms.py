from django import forms
#import LengthValidator and ComplexityValidator from passwords.validators
from passwords.validators import (LengthValidator, ComplexityValidator)

#import Customer model from your application models
from catalog.models import Customer

#create the form class
class CustomerForm(forms.ModelForm):
    #use predefined validators attributes from password.validators module
    #add form label
    #add help_text information
    #specify widget as passwordInput
    password=forms.CharField(validators=[LengthValidator(min_length=8),
	ComplexityValidator(complexities=dict(UPPER=1,LOWER=1,DIGITS=1)),],
	widget=forms.PasswordInput,max_length=40,label='Password',
        help_text='Please use at least one uppercase and a number and must be 8 characters or more')
    
    class Meta:
       #Define the model class created under models for this form
        model= Customer
        #Below you define which model fiels you want to display 
        fields=['fname','lname','email','phoneNumber','occupation','gender', 'media','password','comments']

        #Removed model password field from widgets
        widgets = { 'comments': forms.Textarea(attrs={'cols': 20, 'rows': 10}),
        'media': forms.CheckboxSelectMultiple(), 'gender': forms.RadioSelect(),}
#create signin form without using a model
class SignInForm(forms.Form):
    email=forms.CharField(label='Email Address',widget=forms.TextInput(attrs={'size': '30'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'size':'30'}),label='Password')
