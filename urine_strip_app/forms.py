# urine_strip_app/forms.py

from django import forms

class UrineStripUploadForm(forms.Form):
    image = forms.ImageField()
