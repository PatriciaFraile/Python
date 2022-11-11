#Crear un programa que almacene ocho veces una frase en un .txt

fichero = 'ficheroUno'+'.txt'
with open (fichero,'a') as escribir:
    for i in range (1,9):
        leer = escribir.write("otra opcion\n")
        i = leer
    escribir.close()
