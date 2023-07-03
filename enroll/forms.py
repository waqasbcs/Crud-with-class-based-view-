from django.core import validators
from django import forms
from .models import user

class studentregistration(forms.ModelForm):
    class Meta: 
        model = user
        fields = ['first_name', 'last_name', 'phone', 'address', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Mobile number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Address'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'Enter your Password'}),
        }
