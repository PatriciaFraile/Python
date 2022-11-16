def menu():
   print("""1.Crear fichero
   2. Añadir contacto
   3.Consultar agenda
   4.Borrar contacto
   5.Salir""")
n = 0
while n!=5:
   menu()
   n = int(input("Opcion"))
   if n == 1:
      print("Crear fichero")
      #break
   elif n==2:
      print("Añadir contacto")
      #break
print("salir")



