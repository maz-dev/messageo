from django import forms
from chat.models import Message


class SubmitForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.TextInput(
                attrs={'id': 'message-body', 'required': True, 'placeholder': 'Votre message'}
            ),
        }
