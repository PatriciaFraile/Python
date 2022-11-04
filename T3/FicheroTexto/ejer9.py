#Escribe un programa que pida por teclado un numero positivo entre 1 y 100 y lo guarde en un fichero

numero = int(input("Escribe un numero positivo entre 1 y 100"))
fichero = 'ejercicio1-100'+'.txt'
if numero<0 and numero<100:
    print("Tiene que ser un numero positivo y menor de 100")
else:
    with open (fichero,'w')as escribir:
        escribir.write(str(numero))
    escribir.close()
        