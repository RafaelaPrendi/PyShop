from django.forms import forms
from django import forms

class DyqanForm(forms.Form):
    emri_dyqanit = forms.CharField(label='Emri Dyqanit', max_length=100)

class ProduktForm(forms.Form):
    emri_produktit = forms.CharField(label='Emri Produktit', max_length=100)