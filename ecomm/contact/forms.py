from django import forms


class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'type': 'text', 'name': 'name', 'class':'form-control', 'id':'name','placeholder':'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control', 'name':'email', id:'email', 'placeholder':'Your Email'}))
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'name':'subject', 'id':'subject', 'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'name':'message', 'placeholder':'Message'}))
