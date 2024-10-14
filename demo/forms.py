from django import forms 
from demo.models import Std 

class loginform(forms.ModelForm):

    class Meta:
        model=Std 
        fields=['name','lastname','password']