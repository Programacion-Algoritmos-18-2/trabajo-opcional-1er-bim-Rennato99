# Principal

from sector_estudiantil.alumno import *		
from personal_academico.docente import *		
	
# Leemos por teclado los datos 1
nombre = str(input("Ingrese el nombre del docente Matematicas: "))			
apellido = str(input("Ingrese el apellido del docente Matematicas: "))
titulo = str(input("Ingrese el titulo del docente de  Matematicas: "))

# Creamos on objeto tipo Docente
docenteMatematicas = Docente(nombre, apellido, titulo)									

# Leemos por teclado los datos 2
nombre2 = str(input("Nombre del docente Sociales: "))		
apellido2 = str(input("Apellido del docente Sociales: "))
titulo2 = str(input("Titulo del docente de Sociales: "))

# Creamos on objeto tipo Docente
docenteSociales = Docente(nombre2, apellido2, titulo2)								

# Leemos el nombre del alumno
nombre = str(input("Nombre del Alumno: "))			

# Creamos el objeto tipo Alumno	
alumno = Alumno(nombre, docenteMatematicas, docenteSociales)	

# Presentamos datos del objeto Alumno
print(alumno.presentarDatos())					



