from django import forms
from .models import Form

class FormCreationForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['content']

class FormChangeForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['content']
