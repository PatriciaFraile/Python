unidades = ["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
decenas = ["once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve"]
diez_diez = ["veinti","treinta ","cuarenta","cincuenta","sesenta","sesenta","ochenta","noventa"]

nombre = input("Escribe tu nombre")
apellido = input("Escribe tu apellido")
edad = int(input("Escribe tu edad"))

Midiccionario = {
    'Nombre': nombre,
    'Apellido': apellido,
    'Edad':str(edad)
}
if(edad>1 and edad<11):
    Midiccionario["Edad"] = unidades[edad]
    print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " años")
elif(edad==1):
     Midiccionario["Edad"] = "1"
     print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " año")
elif(edad==0):
     Midiccionario["Edad"] = unidades[edad]
     print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " años")
elif(edad<20):
    Midiccionario["Edad"] = decenas[edad-11]
    print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " años")
elif(edad>=20 and edad<=29):
      num = edad%10
      entero = int(edad/10)
      if(num==0):
        Midiccionario["Edad"]="veinte"
        print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " años")
      else:
        Midiccionario["Edad"] = diez_diez[entero-2] + unidades[num]
        print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " años")
elif(edad>29 and edad<100):
    num = edad%10
    entero = int(edad/10)
    if(num==0):
            Midiccionario["Edad"] = diez_diez[entero-2]
            print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " años")
    else:
        Midiccionario["Edad"] = diez_diez[entero-2] + " y " + unidades[num]
        print(Midiccionario['Nombre'] + Midiccionario["Apellido"]+ " tiene " + Midiccionario['Edad']+ " años")
else:
    print("Tiene que ser menor de 100")





