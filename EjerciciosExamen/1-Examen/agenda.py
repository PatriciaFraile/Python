from os import remove
contacto={}
def menu():
   print("""
   1.Crear fichero
   2. Añadir contacto
   3.Consultar agenda
   4.Borrar fichero
   5.Salir""")
n = 0
nombre_fichero = ""
opcion = 0
nombre = ""
borrar = ""
while n!=5:
   menu()
   n = int(input("Opcion"))
   if n == 1:
      print("--Crear fichero--")
      nombre_fichero = 'agenda'+'.txt'
      print("Fichero creado ")
   elif n==2:
      print("--Añadir contacto--")
      try:
         with open(nombre_fichero,'w')as f:
            nombre = input("Escribe tu nombre")
            tlfn = int(input("Escribe tu numero de telefono"))
            contacto[nombre]=tlfn
            for nombre , tlfn in contacto.items():
             f.write(nombre + '-' + str(tlfn)+ '\n')
         f.close()
      except FileNotFoundError:
         print("No existe el fichero, intentalo otra vez")
   elif n==3:
      print("--Consultar agenda--")
      print("--Listar contactos--")
      try:
         with open (nombre_fichero,'r') as f:
            lineas =f.read()
            print(lineas)
         f.close()
      except FileNotFoundError:
         print("No se encuentra el fichero")
   elif n==4:
      print("--Borrar fichero--")
      try:
         remove(nombre_fichero)
         print("Fichero borrado")
      except FileNotFoundError:
         print("No existe el fichero")
print("salir")