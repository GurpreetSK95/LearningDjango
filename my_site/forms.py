from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=30)
    email = forms.EmailField(required=False, label='Your e-mail address')   # label for email
    message = forms.CharField(widget=forms.Textarea)    # rendered as text-area now
