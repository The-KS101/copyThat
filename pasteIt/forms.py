from django import forms

class ContentPasted(forms.Form):
    content = forms.CharField(label=" ")
    delTime = forms.DateTimeField(label="Expiry", input_formats=['%d/%m/%Y %H:%M'])
