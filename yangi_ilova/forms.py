from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingiz', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Elektron Pochta', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon Raqam'}),
            'message': forms.Textarea(attrs={'placeholder': 'Xabar', 'required': True}),
        }