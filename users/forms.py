from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class RegisterForm(forms.Form):
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    # age = forms.IntegerField(min_value=18, required=False)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())