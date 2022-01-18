from datetime import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.conf import settings

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from apps.administrador.models import Usuario,Medicamento,Cliente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth import authenticate
# Create your views here.
import json
import urllib
import urllib.request
from django.contrib import messages
# Create your views here.
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from django.core.mail import EmailMessage

# Importamos librerías
import mimetypes

# Importamos los módulos necesarios
#from email.mime.multipart import MIMEMultipart
import email.mime.multipart as mu
import email.mime
#from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import json 

# Create your views here.
# tipo 0 super admin
# tipo 1 clinica
# tipo 2 empleado


def pos(request):
	return render(request,'pos.html')

def dashboard(request):
	return render(request,'administrador/dashboard.html')

def medicamentos(request):
	m=Medicamento.objects.all()
	context={"me":m}
	return render(request,'administrador/medicamentos.html',context)

def clientes(request):
	m=Cliente.objects.all()
	context={"me":m}
	return render(request,'administrador/clientes.html',context)

def delete_cliente(request):
	m=Cliente.objects.get(id=request.POST['admon'])
	m.delete()
	return redirect('clientes')

def edit_cliente(request,id):
	m=Cliente.objects.get(id=id)
	if request.method=='POST':
		m.compuesto=request.POST['compuesto']
		m.marca=request.POST['marca']
		m.presentacion=request.POST['presentacion']
		m.contenido=request.POST['contenido']
		m.precio=request.POST['precio']
		m.stock=request.POST['stock']
		m.save()
		try:

			myfile = request.FILES['foto']
			fs = FileSystemStorage()
			nombre=myfile.name
			filename = fs.save(nombre, myfile)
			m.foto=filename
			m.save()

		except:
			pass

		return redirect('clientes')


def edit_medicamento(request,id):
	m=Medicamento.objects.get(id=id)
	if request.method=='POST':
		m.compuesto=request.POST['compuesto']
		m.marca=request.POST['marca']
		m.presentacion=request.POST['presentacion']
		m.contenido=request.POST['contenido']
		m.precio=request.POST['precio']
		m.stock=request.POST['stock']
		m.save()
		try:

			myfile = request.FILES['foto']
			fs = FileSystemStorage()
			nombre=myfile.name
			filename = fs.save(nombre, myfile)
			m.foto=filename
			m.save()

		except:
			pass

		return redirect('medicamentos')
		
	context={"me":m}
	return render(request,'administrador/editar_medicamentos.html',context)


def delete_medicamento(request):
	m=Medicamento.objects.get(id=request.POST['admon'])
	m.delete()
	return redirect('medicamentos')


def añadir_medicamentos(request):
	if request.method=='POST':
		myfile = request.FILES['foto']
		fs = FileSystemStorage()
		nombre=myfile.name
		filename = fs.save(nombre, myfile)
		m=Medicamento(compuesto=request.POST['compuesto'],marca=request.POST['marca'],presentacion=request.POST['presentacion'],contenido=request.POST['contenido'],precio=request.POST['precio'],stock=request.POST['stock'],foto=filename)
		m.save()
		return redirect('medicamentos')
	return render(request,'administrador/añadir_medicamentos.html')




def añadir_clientes(request):
	if request.method=='POST':
		c=Cliente(nombre=request.POST['nombre'],apellidos=request.POST['apellidos'],correo=request.POST['correo'],telefono=request.POST['telefono'],rfc=request.POST['rfc'],fisica_moral=request.POST['persona'])
		c.save()
		return redirect('clientes')
	return render(request,'administrador/añadir_clientes.html')



def index(request):
	return render(request,'index.html')

def index_medico(request):
	return render(request,'index_medico.html')

def quienes_somos(request):
	return render(request,'quienes_somos.html')


def login(request):

	if request.method=='POST':
		user = authenticate(request,username=request.POST['email'], password=request.POST['pwd'])
		if user is not None:   
			auth.login(request, user)
			request.session['usuario'] = request.POST['email']
			u=Usuario.objects.get(usuario=request.POST['email'])
			
			return redirect('dashboard')
		else:
			return redirect('login')		


	return render(request,'login.html') 

def registro_superusuario(request):
	u=User(email='enrique_face1994@hotmail.com',first_name='super_usuario',username='super_usuario')
	u.set_password('password2020')
	u.is_staff = True
	u.is_superuser= True
	u.is_active=True
	u.save()
	u2=Usuario(apellidos='password',nombre='super',correo='enrique_face1994@hotmail.com',usuario='super_usuario',password='password2020',tipo=0)
	u2.save()
	return redirect('index')

