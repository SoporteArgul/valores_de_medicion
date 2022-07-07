from django import forms
from django.forms import ModelForm
from .models import Lentes

class LentesForm(forms.ModelForm):  
    class Meta:  
        model = Lentes
        fields = "__all__"  