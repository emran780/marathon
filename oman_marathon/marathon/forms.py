# marathon/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ContactUsMessage

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

class RunnerLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
