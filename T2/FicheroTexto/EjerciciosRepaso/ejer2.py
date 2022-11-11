'''Escribe un programa que pida por teclado un número positivo entre 1 y 100
y lo guarde en un fichero llamado "ejercicio1-100.txt"'''

numero = int(input("Escribe un numero entre 1 - 100"))
numero_fichero = 'ejercicio1-100'+'.txt'

if(numero<0 and numero<100):
    print("Debe ser mayor de 0 y menor de 100")
else:
    with open(numero_fichero,'w') as f:
        f.write(str(numero))
    f.close()
