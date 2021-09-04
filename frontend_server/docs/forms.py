from django import forms
from django.forms import ModelForm

from docs.models import Document
from factory.models import User

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['html_data', 'owner', 'preview']
