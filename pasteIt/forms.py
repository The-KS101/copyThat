from django import forms
from .models import urlTable

TIME_CHOICES = (
    (0, ("On View")),
    (10, ("10 Minutes")),
    (30, ("30 Minutes")),
    (60, ("1 Hour")),
    (360, ("6 Hours")),
    (720, ("12 Hours")),
    (1440, ("24 Hours")),
)
class ContentPasted(forms.ModelForm):
    delTime = forms.ChoiceField(choices=TIME_CHOICES, )
    class Meta:
        model = urlTable
        fields = ['url', 'text']

    

class DispPasted(forms.Form):
    content = forms.CharField(label=" ")
