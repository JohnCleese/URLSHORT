from django import forms
from .models import New_adress

class Adressform(forms.ModelForm):
    class Meta:
        model = New_adress
        fields = ('url_old',)
        labels = {'url_old': "old adress"}