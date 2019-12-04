from django.shortcuts import render,HttpResponse, redirect
#archivo url para redireccionar
from django.urls import reverse
#se carga el formulario
from .forms import ContactForm



# Create your views here. vista de index

def indexcore(request):
	#Se instancia el formulario de contacto
	FormContact =ContactForm()
	#se valida que se haya echo la petición post del formulario contacto
	if request.method == "POST":
		#se reasigna el valor de FormContact, pero con todos los datos del formulario
		FormContact = ContactForm(data=request.POST)
		#validacion de los campos
		email = request.POST.get('email','')
		tipom = request.POST.get('tipom','')
		nombre = request.POST.get('nombre','')
		msj = request.POST.get('msj','')
		#se guarda y se redirecciona al nombre de la url con un mensaje
		FormContact.save()
		return redirect(reverse('/indexcore/')+"?OK")
	   
	return render(request, 'core/index.html',{'formulario':FormContact})

def nosotros(request):
	return render(request, 'core/nosotros.html')
