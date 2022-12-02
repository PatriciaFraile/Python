nombre_fichero = 'contador'+'.txt'
opcion = ""
fichero = open (nombre_fichero , 'a+')
fichero.seek(0)
contenido = fichero.readline()
if len(contenido)==0:
    contenido = 0
    fichero.write(str(0))
try:
    contador = int(contenido)
    opcion = input("Que quieres inc/desc")
    if opcion == 'inc' or opcion == 'INC':
        contador = contador+1
    elif opcion=='desc' or opcion == 'DESC':
        contador = contador-1
    print(contador)
    with open(nombre_fichero,'w') as f:
        f.write(str(contador))
    f.close()
except FileNotFoundError:
    print("No existe el fichero")