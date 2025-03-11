from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser, Customer

# Authentication form start

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'branch']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username")

class CutomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'customer_name': "Customer Name",
            'customer_name_bn': "Customer Name Bangla",
        }