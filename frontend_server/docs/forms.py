from django import forms
from django.forms import ModelForm

from docs.models import Document
from factory.models import User

class DocumentForm(ModelForm):
    # authors = forms.CharField(max_length=30, widget=forms.Select(choices=User))
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['html_data', 'owner', 'preview']
