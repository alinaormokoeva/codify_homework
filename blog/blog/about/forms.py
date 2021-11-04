from django import forms

class Information(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    message = forms.CharField()
    allow_mailing = forms.BooleanField()


