from django import forms
from django.forms import Form

class HandelForm(Form):
    image_name = forms.CharField(label='image_name', widget=forms.TextInput(
        attrs={
            'Placeholder' : 'Type word for image generator',
        }
    ))
