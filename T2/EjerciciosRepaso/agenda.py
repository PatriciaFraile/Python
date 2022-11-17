def menu():
   print("""1.Crear fichero
   2. Añadir contacto
   3.Consultar agenda
   4.Borrar contacto
   5.Salir""")
n = 0
nombre_fichero = ""
while n!=5:
   menu()
   n = int(input("Opcion"))
   if n == 1:
      print("Crear fichero")
      nombre_fichero = 'agenda'+'.txt'
      print("Fichero creado ")
   elif n==2:
      print("Añadir contacto")
      with open(nombre_fichero,'w')as f:
         f.write(input("Añade contacto"))
      f.close()
   elif n==3:
      print("Consultar agenda")

      #break
print("salir")



