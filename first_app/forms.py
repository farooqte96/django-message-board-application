from django import forms

# Create form from Model
from .models import Message

class CreateMessage(forms.ModelForm):
    class Meta():
        model = Message
        fields = "__all__"

VERSIONS = [
    ('1', "Version 1 (show all fields)"),
    ('2', "Version 2 (show only title, content and sender)"),
]

class SelectVersion(forms.Form):
    version = forms.ChoiceField(choices = VERSIONS)
