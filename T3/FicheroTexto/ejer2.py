#Escribe una función que pida dos numeros n y m entre 1 y 10,
#lea la tabla -n.txt con la tabla de multiplicar de ese numero
#y muestre por pantalla la linea m del fichero

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    with open(nombre_fichero, 'r') as leer:
        lineas = leer.readlines()
    print(lineas[m - 1])
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
