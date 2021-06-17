from django import forms
from django.core.exceptions import ValidationError

from .models import *


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirmation", "first_name", "last_name"]

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        password_confirmation = data.pop("password_confirmation")
        if password != password_confirmation:
            raise ValidationError("Password do not match")
        return data

    def save(self, commit=True):
        print(self.cleaned_data)
        user = User.objects.create_user(**self.cleaned_data)
        return user


