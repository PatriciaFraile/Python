contacto={}
def menu():
   print("""
   1.Crear fichero
   2. Añadir contacto
   3.Consultar agenda
   4.Borrar contacto
   5.Salir""")
n = 0
nombre_fichero = ""
opcion = 0
while n!=5:
   menu()
   n = int(input("Opcion"))
   if n == 1:
      print("--Crear fichero--")
      nombre_fichero = 'agenda'+'.txt'
      print("Fichero creado ")
   elif n==2:
      print("--Añadir contacto--")
      nombre = input("Escribe tu nombre")
      tlfn = int(input("Escribe tu numero de telefono"))
      contacto[nombre]=tlfn
      try:
         with open(nombre_fichero,'w')as f:
            for nombre , tlfn in contacto.items():
             f.write(nombre + '-' + str(tlfn)+ '\n')
         f.close()
      except FileNotFoundError:
         print("No existe el fichero, intentalo otra vez")
   elif n==3:
      print("--Consultar agenda--")
      while opcion == 3:
         print("""
         1.Listar contactos
         2.Busqueda de contacto
         3.Salir""")
         opcion = int(input("Que opcion quieres"))
         if opcion==1:
            print("--Listar contactos--")
            try:
               print("")
            except FileNotFoundError:
               print("No existe el fichero, intentalo de nuevo")
         elif opcion ==2:
            print("--Busqueda de contacto--")
            try:
             print("")
            except FileNotFoundError:
              print("No existe el fichero, intentalo de nuevo")

   elif n == 4:
      print("Borrar contacto")
      try:
         print("")
      except FileNotFoundError:
         print("No existe el fichero , intentalo de nuevo ")
      #break
print("salir")



