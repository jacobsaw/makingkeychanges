from django import forms
from django.core.exceptions import ValidationError

import re

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact_email = forms.EmailField(required=True , widget=forms.TextInput(attrs={'class' : 'form-control'}))
    contact_phone = forms.CharField(required=True , widget=forms.TextInput(attrs={'class' : 'form-control'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class' : 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name*"
        self.fields['contact_email'].label = "Email Address*"
        self.fields['contact_phone'].label = "Phone Number*"
        self.fields['content'].label = "Message*"

    # def clean_contact_name(self):
    #     NAME_REGEX = re.compile(r'<([^>]+)>')
    #     name = self.cleaned_data['contact_name']
    #     if not NAME_REGEX.match(name):
    #         raise ValidationError("Please enter your first and last name")
    #     return name

    def clean_contact_phone(self):
        PHONE_REGEX = re.compile(r'^\+?1?\d{9,15}$')
        phone = self.cleaned_data['contact_phone']
        phone = phone.replace("-","")
        if not PHONE_REGEX.match(phone):
            raise ValidationError("Please enter a valid phone number (123-123-1234)")
        return phone