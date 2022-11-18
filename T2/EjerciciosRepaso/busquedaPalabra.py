nombre_fichero = 'busqueda'+'.txt'
texto = input("Escribe un texto de lo que tu quieras")
fichero = open(nombre_fichero, 'a+')
fichero.write(texto)
busqueda = input("Que quieres buscar")
try:
    with open (nombre_fichero ,'r')as f:
        linea = f.readline()
        for i in linea:
            if busqueda==i:
                print(i)
    f.close()
except FileNotFoundError:
    print("El fichero no existe")
