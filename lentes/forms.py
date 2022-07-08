from django import forms
from django import forms
from .models import tiempo_de_carro

class tiempo_carro(forms.Form):  
        name = forms.CharField(label='Your name')
        url = forms.URLField(label='Your website', required=False)
        comment = forms.CharField()
f = tiempo_carro(auto_id=False)
print(f.as_p())
     


        
        