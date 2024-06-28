from django import forms 
from .models import *

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'content', 'description', 'journal_type']

class JournalTypeForm(forms.ModelForm):
    class Meta:
        model = JournalType
        fields = ['type']