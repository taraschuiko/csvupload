from django import forms

class UploadTableForm(forms.Form):
  table = forms.FileField()