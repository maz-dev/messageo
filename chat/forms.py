from django import forms
from chat.models import Message


class SubmitForm(forms.ModelForm):
    body = forms.CharField(max_length=1024, label="Tapez votre message: ", required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Votre message'}))
    class Meta:
        model = Message
        fields = ['body']

