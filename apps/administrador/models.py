from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre=models.CharField(max_length=200)
	apellidos=models.CharField(max_length=20)
	correo=models.CharField(max_length=100)
	telefono=models.CharField(max_length=15)
	tipo=models.IntegerField(null=True)
	password=models.CharField(max_length=75,blank=True)
	usuario=models.CharField(max_length=40,blank=True)
	foto=models.FileField(blank=True)

class Medicamento(models.Model):
	compuesto=models.CharField(max_length=40,null=True,blank=True)
	marca=models.CharField(max_length=40,null=True,blank=True)
	presentacion=models.CharField(max_length=40,null=True)
	contenido=models.CharField(max_length=40,null=True)
	precio=models.FloatField(null=True,blank=True)
	stock=models.IntegerField(null=True,blank=True)
	foto=models.FileField(null=True,blank=True)

class Cliente(models.Model):
	nombre=models.CharField(max_length=20,null=True,blank=True)
	apellidos=models.CharField(max_length=20,null=True,blank=True)
	correo=models.CharField(max_length=50,null=True,blank=True)
	telefono=models.CharField(max_length=15,null=True,blank=True)
	rfc=models.CharField(max_length=20,null=True,blank=True)
	fisica_moral=models.CharField(max_length=25,null=True,blank=True)