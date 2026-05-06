from django import forms
from .models import ContactQuery

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ['first_name','last_name','email','phone','service','message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'John','class':'form-control'}),
            'last_name':  forms.TextInput(attrs={'placeholder':'Doe','class':'form-control'}),
            'email':      forms.EmailInput(attrs={'placeholder':'you@company.com','class':'form-control'}),
            'phone':      forms.TextInput(attrs={'placeholder':'+91 98765 43210','class':'form-control'}),
            'service':    forms.Select(attrs={'class':'form-control'}),
            'message':    forms.Textarea(attrs={'placeholder':'Tell us about your project...','rows':4,'class':'form-control'}),
        }
