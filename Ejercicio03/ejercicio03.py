# Creamos la clase guarantor
class Garante(object):
	
	# Construcotr						
	def __init__(self, name, lastName, salary):				
		self.setName(name) 						
		self.setLastName(lastName)
		self.setSalary(salary)

	# Metodos Set 
	def setName(self, name):							
		self.name = name

	def setLastName(self, lastName):
		self.lastName = lastName

	def setSalary(self, salary):
		self.salary = salary

	# Metodos get
	def getName(self):							
		return self.name

	def getlastName(self):
		return self.lastName

	def getSalary(self):
		return self.salary

	# Metodo para presentar datos 
	def presentData(self):						
		string = ("\n\tGarante:\n\t\tNombre: %s %s\n\t\tSalario: %d" % (self.getName(), self.getlastName(), self.getSalary()))
		return string


# Creamos la clase Prestamo
class Prestamo(object):							

	def __init__(self, name, salary, amount, interest, time, guarantor1):			
		self.setName(name)		
		self.setSalary(salary)
		self.setAmount(amount)
		self.setInterest(interest)
		self.setTime(time)
		self.setGuarantor(guarantor1)

	# Metodos set
	def setName(self, name):			
		self.name = name
		
	def setSalary(self, salary):
		self.salary = salary

	def setAmount(self, amount):
		self.amount = amount

	def setInterest(self, interest):
		self.interest = interest

	def setTime(self, time):
		self.time = time

	def setGuarantor(self, guarantor):
		self.guarantor = guarantor 

	# Metodos get
	def getName(self):		
		return self.name

	def getSalary(self):
		return	self.salary

	def getAmount(self):
		return self.amount

	def getInterest(self):
		return self.interest

	def getTime(self):
		return self.time

	def getGuarantor(self):
		return self.guarantor

	# Metodo para presentar datos
	def presentData(self):			
		string = ("\nPrestamo:\n\tNombre del Beneficiario: %s\n\tSalario: %d\n\tMonto del prestamo: %d\n\tIntereses (porcentaje): %d\n\tTiempo (años): %d\n\t%s\n\n"%(self.getName(), self.getSalary(), self.getAmount(), self.getInterest(), self.getTime(), self.getGuarantor().presentData()))
		return string


# Creamos la clase PrestamoAutomovil
class PrestamosAutomovil(Prestamo):									

	# Constructor
	def __init__(self, name, salary, amount, interest, time, guarantor1, kind, brand, guarantor2):			
		super(PrestamosAutomovil, self).__init__(name, salary, amount, interest, time, guarantor1)		
		self.setKind(kind)							
		self.setBrand(brand)
		self.setGuarantor(guarantor2)

	# Metodo set
	def setKind(self, kind):			
		self.kind = kind

	def setBrand(self, brand):
		self.brand = brand

	def setGuarantor(self, guarantor):
		self.guarantor = guarantor

	# Metodos Get
	def getKind(self):				
		return self.kind

	def getBrand(self):
		return self.brand

	def getGuarantor(self):
		return self.guarantor

	# Metodo para presentar datos
	def presentData(self):		
		string = ("\nPrestamo automovil:\n\tNombre del Beneficiaio: %s\n\tSalario: %d\n\tMonto del prestamo: %d\n\tInteresese (porcentaje): %d\n\tTiempo (años): %d\n\tTipo de vehiculo: %s\n\tMarca del vehiculo: %s\n\t%s\n\n" % (self.getName(), self.getSalary(), self.getAmount(), self.getInterest(), self.getTime(), self.getKind(), self.getBrand(), self.getGuarantor().presentData()))
		return string

# Creando la clase principal
def main():
	
	garante1 = Garante("Renato", "Balcazar", 1000)					
	prestamo = Prestamo("Lenin Moreno", 6000, 1000, 6, 10, garante1)		
	garante2 = Garante("Julio","Ordoñes", 500)
	prestamoAutomovil = PrestamosAutomovil("Abdala Bucaram", 8000, 5000, 5, 15, garante2, "Automovil", "Roll Roys", garante2)	 


	# Se presentan los datos
	print(prestamo.presentData())			
	print(prestamoAutomovil.presentData())		



# LLamamos a la clase principal
main()
