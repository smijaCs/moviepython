from django import forms
from .models import updates

class MovieForm(forms.ModelForm):
    class  Meta:
        model=updates
        fields=['name','desc','year','img']
