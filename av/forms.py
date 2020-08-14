from django import forms
from .models import *
class Passcode(forms.Form):

    Column_Fields = [
        ("password", "Password"),
    ]

    name = forms.CharField(
        required=False,
        label="Love Code",
        widget=forms.TextInput(
            attrs={"class": "form-control" "col-xs-4", "max_length": "300", "autocomplete": "off"}
        )
    )