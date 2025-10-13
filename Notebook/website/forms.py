from django import forms
from .models import Nbook

class NbookForm(forms.ModelForm):
    class Meta:
        model = Nbook
        fields = ['title', 'text', 'image', 'filenotebook']

