#importacion libreria forms
from django import forms
#Lista de las posibles peticiones del select 
from .pqrsf import PQRSF_CHOICES

#estructura del formulario
class ContactForm(forms.form):
	#campos
	email = forms.EmailField(label = "Correo Electronico", widget=forms.EmailInput(attrs={'class';'form-control'}), required=True)
	tipom = forms.ChoiceField(choices = PQRSF_CHOICES, label="Tipo de Atención Requerida", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True)
	nombre = forms.CharField(label = "Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	msj = forms.CharField(label = "Mensaje", widget = forms.Textarea(attrs={'class':'form-control', 'rows':'3'}), required=True)




	