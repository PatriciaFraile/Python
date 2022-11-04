#Escribe una función que pida un numero entero
#del 1 al 10 y lo guarde en un fichero con el nombre de 
#tabla -n.txt la tabla de multiplicar de dicho numero.

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
with open(nombre_fichero, 'w') as escribir:
    for i in range(1,11):
        escribir.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
escribir.close()