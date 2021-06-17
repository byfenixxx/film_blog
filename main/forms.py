from django import forms
from django.urls import reverse

from .models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ["title", "description", "pub_year", "poster", "genre"]


