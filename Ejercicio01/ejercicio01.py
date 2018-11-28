# Creando la clase futbolista
class Futbolista():

	'''
	# Constructor con todos los atributos dados
	Se ponen los atributos como: (nombre) = (valor por defecto), en caso de que al 
	momento de construir el objeto estos atributos no sean enviados
	'''
	def __init__(self, name="", lastname="", team=None, position="", dorsal=0):
		self.setName(name)
		self.setLastName(lastname)
		self.setTeam(team)
		self.setPosition(position)
		self.setDorsal(dorsal)

	# Metodos set
	def setName(self, name):
		self.name = name

	def setLastName(self, lastname):
		self.lastname = lastname

	def setTeam(self, team):
		self.team = team

	def setPosition(self, position):
		self.position = position.upper()

	def setDorsal(self, dorsal):
		self.dorsal = dorsal

	# Metodos get
	def getName(self):
		return self.name

	def getLastName(self):
		return self.lastname

	def getTeam(self):
		return self.team

	def getPosition(self):
		return self.position

	def getDorsal(self):
		return self.dorsal

	# Metodo par presentar datos
	def presentPlayer(self):
		string = ("\n%s %s\npertenece al equipo %s\nsu posicion es %s y\nsu dorsal es el numero %d." %(self.getName(), self.getLastName(), self.getTeam().presentTeam(), self.getPosition(), self.getDorsal()))
		return string



# Creando la clase Equipo
class Equipo():

	# Constructor
	def __init__(self, name="", country=""):
		self.setName(name)
		self.setCountry(country)

	# Metodos set
	def setName(self, name):
		self.name = name.title()

	def setCountry(self, country):
		self.country = country.title()

	# Metodos get
	def getName(self):
		return self.name

	def getCountry(self):
		return self.country

	# Metodo para presentar sus datos
	def presentTeam(self):
		string = ("%s del pais %s,"%(self.getName(), self.getCountry()))
		return string


# Creando la clase principal
def main():
	# Creamos los objetos equipo
	necaxa = Equipo("necaxa", "mexico")
	lazio = Equipo("lazio", "italia")
	manchester = Equipo("manchester united", "inglaterra")

	# Creamos los objetos jugadores
	f = Futbolista("Antonio", "Valencia")
	f2 = Futbolista("Alex", "Aguinaga", necaxa, "mediocentro")
	f3 = Futbolista("Felipe", "Caicedo", lazio)

	# Agregamos atributos faltantes a los objetos f
	f.setTeam(manchester)
	f.setPosition("lateral")
	f.setDorsal(25)

	# Agregamos atributos faltantes a los objetos f2
	f2.setDorsal(7)

	# Agregamos atributos faltantes a los objetos f3
	f3.setPosition("delantero")
	f3.setDorsal(32)



	# Presentamos los objetos con su metodo
	print(f.presentPlayer())
	print(f2.presentPlayer())
	print(f3.presentPlayer())


# LLamamos a la clase principal
main()


'''
	Esto es lo que trataba de hacer al principio, luego advertí que no se podia
	poner varios constructores en python, pero encontré otro metodo para resolver 
	cuando al momento de creal el objeto no todos los atributos eran dados
	
	# Constructor con 2 atributos
	def __init__(self, name, lastname):
			self.setName(name)
			self.setLastName(lastname)


	# Constructor con 3 atributos
	def __init__(self, name, lastname, team):
		self.setName(name)
		self.setLastName(lastname)
		self.setTeam(team)

	# Constructor con 4 atributos
	def __init__(self, name, lastname, team, position):
		self.setName(name)
		self.setLastName(lastname)
		self.setTeam(team)
		self.setPosition(position)
'''