from django import forms

from .models import SignUp #! From the models.py file in the same directory import class SignUp

class SignUpForm(forms.ModelForm):  #! Create a new class of type ModelForm, the class definition for which has been imported in the first line
    class Meta:                     
        model = SignUp              #! Using the SignUp class in the models.py file specified earlier
        