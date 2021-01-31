from django import forms
from .models import Clave

class ClaveForm(forms.ModelForm):
    url = forms.URLField(label='')
    username = forms.CharField(label='')
    email = forms.EmailField(label='')
    passwordtwo = forms.CharField(label='')

    class Meta:
        model = Clave
        fields = ['url', 'email', 'username', 'passwordtwo']
        widgets = {
            'url': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Page link'}),
            'email': forms.EmailInput(attrs={'class':'form-control mt-3', 'placeholder':'Email'}),
            'username': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Username'}),
            'passwordtwo': forms.PasswordInput(attrs={'class':'form-control mt-3', 'placeholder':'Password'}),
        }