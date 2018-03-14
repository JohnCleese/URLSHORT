from django import forms
from .models import NewAdress


class Adressform(forms.ModelForm):
    class Meta:
        model = NewAdress
        fields = ('main_url',)
        labels = {'main_url': "old adress"}
