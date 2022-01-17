from django.forms import ModelForm

from docs.models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['html_data', 'owner', 'preview']
