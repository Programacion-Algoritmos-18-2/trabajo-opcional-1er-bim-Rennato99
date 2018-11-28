class Docente(object):

	# Constructor								
	def __init__(self, name, lastname, title):						
		self.setName(name)
		self.setLastName(lastname)
		self.setTitle(title)
 
	# Metodos Set 
	def setName(self, name):							
		self.name = name

	def setLastName(self, lastname):
		self.lastname = lastname

	def setTitle(self, title):
		self.title = title

	# Metodos get
	def getName(self):							
		return self.name

	def getLastName(self):
		return self.lastname

	def getTitle(self):
		return self.title

	# Metodo para presentar datos	
	def presentarDatos(self):			
		cadena = "Nombre del docente: %s %s\n\t\tTitulo: %s\n"%(self.getName(), self.getLastName(),self.getTitle())
		return cadena

		