from django import forms

TIME_CHOICES = (
    (0, ("On View")),
    (10, ("10 Minutes")),
    (30, ("30 Minutes")),
    (60, ("1 Hour")),
    (360, ("6 Hours")),
    (720, ("12 Hours")),
    (1440, ("24 Hours")),
)
class ContentPasted(forms.Form):
    url = forms.CharField(label="Name")
    content = forms.CharField(label=" ", widget=forms.Textarea)
    delTime = forms.ChoiceField(choices=TIME_CHOICES, )

class DispPasted(forms.Form):
    content = forms.CharField(label=" ")
