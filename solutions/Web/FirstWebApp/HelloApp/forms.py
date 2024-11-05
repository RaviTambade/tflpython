# forms.py
from django import forms


 #step 1
class LoginForm(forms.Form):
     email = forms.EmailField()
     password = forms.CharField(max_length=100)
    

class RegisterForm(forms.Form):
     email = forms.EmailField()
     contactnumber= forms.CharField(max_length=10)
     firstname= forms.CharField(max_length=100)
     lastname= forms.CharField(max_length=100)
     location= forms.CharField(max_length=100)
     