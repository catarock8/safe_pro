from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Empresa

class RegistroEmpresaForm(UserCreationForm):
    email_contacto = forms.EmailField(required=True)
    rut_empresa = forms.CharField(max_length=12)

    class Meta:
        model = Empresa
        fields = ('nombre', 'rut_empresa', 'email_contacto', 'password1', 'password2')

    def save(self, commit=True):
        empresa = super(RegistroEmpresaForm, self).save(commit=False)
        empresa.email_contacto = self.cleaned_data['email_contacto']
        empresa.rut_empresa = self.cleaned_data['rut_empresa']

        # Aquí es donde encriptamos la contraseña
        empresa.set_password(self.cleaned_data['password1'])
        
        if commit:
            empresa.save()
        return empresa
