
from django import forms


class EmailForm(forms.Form):
    recipient_email = forms.EmailField(label="Recipient email")
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
