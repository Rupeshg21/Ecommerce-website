from django import forms
from .models import Sqtable_cont

class Htform(forms.ModelForm):
    class Meta:
        model = Sqtable_cont
        fields = '__all__'