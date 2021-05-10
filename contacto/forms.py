from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label='Nombre', required=True, max_length=100)
    email = forms.CharField(label='Nombre', required=True, max_length=100)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)