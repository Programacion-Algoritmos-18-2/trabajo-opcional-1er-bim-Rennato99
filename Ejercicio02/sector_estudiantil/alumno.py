from personal_academico.docente import *				
	
# Cremamos la clase alumno
class Alumno(object):									

	# Constructor
	def __init__(self, name, docenteMatematica, docenteSociales):						
		self.setName(name)			
		self.setDocenteMatematicas(docenteMatematica)
		self.setDocenteSociales(docenteSociales)

	# Metodos set	
	def setName(self,name):								
		self.name = name

	def setDocenteMatematicas(self, docenteMatematica):
		self.docenteMatematica = docenteMatematica

	def setDocenteSociales(self, docenteSociales):
		self.docenteSociales = docenteSociales

	# Metodos Get
	def getName(self):								
		return self.name

	def getDocenteMatematicas(self):
		return self.docenteMatematica.presentarDatos()

	def getDocenteSociales(self):
		return self.docenteSociales.presentarDatos()

	# Metodo para presentar datos
	def presentarDatos(self):							
		cadena=("\nName del Estudiante: %s\n\tDocentes:\n\t\t%s\n\t\t%s\n" %(self.getName(), self.getDocenteMatematicas(), self.getDocenteSociales()))
		return cadena

		