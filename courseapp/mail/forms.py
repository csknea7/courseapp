from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"size": "40", "class": "form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"size": "40", "class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"size": "40", "class": "form-control"}))
