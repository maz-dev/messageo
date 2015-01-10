from django import forms
from chat.models import Message


class SubmitForm(forms.ModelForm):
    body = forms.CharField(max_length=1024, label="Tapez votre message: ", required=True)
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.TextInput(
                attrs={'id': 'message-body', 'required': True, 'placeholder': 'Votre message'}
            ),
        }
