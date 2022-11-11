'''Escribe un programa en python que escriba de la forma QUE QUERÁIS en un fichero llamado
"ficheroenpython.txt'''

nombre = input("Escribe un mensaje")
fichero_nombre = 'ficheroenpython'+'.txt'

with open (fichero_nombre,'w') as f:
    f.write(nombre)
f.close()