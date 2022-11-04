#Leer el fichero creado del ejercicio 1 

with open ('tabla-6.txt','r') as leer:
    lineas = leer.readlines()
    print(lineas)